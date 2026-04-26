# ---------------------------------------------------------------------------
# Origin Access Control — grants CloudFront identity access to the private S3 bucket
# ---------------------------------------------------------------------------

resource "aws_cloudfront_origin_access_control" "updates" {
  name                              = "${var.project_name}-updates-oac-${var.environment}"
  description                       = "OAC for AgentCore update server S3 bucket (${var.environment})"
  origin_access_control_origin_type = "s3"
  signing_behavior                  = "always"
  signing_protocol                  = "sigv4"
}

# ---------------------------------------------------------------------------
# CloudFront distribution
# ---------------------------------------------------------------------------

resource "aws_cloudfront_distribution" "updates" {
  enabled             = true
  comment             = "AgentCore update server CDN (${var.environment})"
  default_root_object = "manifest.json"
  price_class         = "PriceClass_100" # US, Canada, Europe only — sufficient for update traffic

  # S3 origin — accessed via OAC, never directly
  origin {
    domain_name              = aws_s3_bucket.updates.bucket_regional_domain_name
    origin_id                = "s3-${local.bucket_name}"
    origin_access_control_id = aws_cloudfront_origin_access_control.updates.id
  }

  # Default cache behaviour: read-only (GET/HEAD), cache 1 hour
  default_cache_behavior {
    target_origin_id       = "s3-${local.bucket_name}"
    viewer_protocol_policy = "redirect-to-https"
    allowed_methods        = ["GET", "HEAD"]
    cached_methods         = ["GET", "HEAD"]
    compress               = true

    forwarded_values {
      query_string = false
      cookies {
        forward = "none"
      }
    }

    # manifest.json uses Cache-Control: max-age=60 set at upload time;
    # release tarballs are immutable so 1 h default is safe.
    min_ttl     = 0
    default_ttl = 3600
    max_ttl     = 86400
  }

  # Return structured JSON error documents so clients can parse them
  custom_error_response {
    error_code            = 404
    response_code         = 404
    response_page_path    = "/404.json"
    error_caching_min_ttl = 30
  }

  custom_error_response {
    error_code            = 403
    response_code         = 403
    response_page_path    = "/403.json"
    error_caching_min_ttl = 30
  }

  restrictions {
    geo_restriction {
      restriction_type = "none"
    }
  }

  # Use the default CloudFront certificate (*.cloudfront.net).
  # Replace with acm_certificate_arn + aliases block to use a custom domain.
  viewer_certificate {
    cloudfront_default_certificate = true
    minimum_protocol_version       = "TLSv1.2_2021"
  }

  tags = {
    Project     = var.project_name
    Environment = var.environment
    ManagedBy   = "terraform"
  }
}

# ---------------------------------------------------------------------------
# S3 bucket policy — allow CloudFront OAC to read objects
# ---------------------------------------------------------------------------

data "aws_iam_policy_document" "cloudfront_s3_access" {
  statement {
    sid    = "AllowCloudFrontOACReadAccess"
    effect = "Allow"

    principals {
      type        = "Service"
      identifiers = ["cloudfront.amazonaws.com"]
    }

    actions   = ["s3:GetObject"]
    resources = ["${aws_s3_bucket.updates.arn}/*"]

    condition {
      test     = "StringEquals"
      variable = "AWS:SourceArn"
      values   = [aws_cloudfront_distribution.updates.arn]
    }
  }
}

resource "aws_s3_bucket_policy" "cloudfront_access" {
  bucket = aws_s3_bucket.updates.id
  policy = data.aws_iam_policy_document.cloudfront_s3_access.json

  # Policy references the distribution ARN, so the distribution must exist first
  depends_on = [aws_cloudfront_distribution.updates]
}
