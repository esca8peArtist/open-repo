# ---------------------------------------------------------------------------
# IAM user for publish_release.py CI/CD automation
# ---------------------------------------------------------------------------

resource "aws_iam_user" "publisher" {
  name = "agentcore-update-publisher-${var.environment}"
  path = "/agentcore/"

  tags = {
    Project     = var.project_name
    Environment = var.environment
    ManagedBy   = "terraform"
    Purpose     = "publish_release.py S3 upload and CloudFront invalidation"
  }
}

# ---------------------------------------------------------------------------
# IAM policy — least-privilege access for publish_release.py
#
# Required operations (from publish_release.py):
#   s3:PutObject          — upload release tarballs and manifest.json
#   s3:GetObject          — download existing manifest to merge releases
#   s3:DeleteObject       — (future: remove old tarballs)
#   s3:ListBucket         — check for existing objects without GetObject errors
#   cloudfront:CreateInvalidation — invalidate /manifest.json after publish
# ---------------------------------------------------------------------------

data "aws_iam_policy_document" "publisher" {
  # S3 object-level access on the updates bucket
  statement {
    sid    = "S3ObjectAccess"
    effect = "Allow"

    actions = [
      "s3:PutObject",
      "s3:GetObject",
      "s3:DeleteObject",
    ]

    resources = ["${aws_s3_bucket.updates.arn}/*"]
  }

  # S3 bucket-level listing (required for SDK list calls and multipart cleanup)
  statement {
    sid    = "S3BucketList"
    effect = "Allow"

    actions   = ["s3:ListBucket"]
    resources = [aws_s3_bucket.updates.arn]
  }

  # CloudFront invalidation — scoped to the specific distribution
  statement {
    sid    = "CloudFrontInvalidation"
    effect = "Allow"

    actions   = ["cloudfront:CreateInvalidation"]
    resources = [aws_cloudfront_distribution.updates.arn]
  }
}

resource "aws_iam_policy" "publisher" {
  name        = "agentcore-update-publisher-policy-${var.environment}"
  path        = "/agentcore/"
  description = "Least-privilege policy for publish_release.py (${var.environment})"
  policy      = data.aws_iam_policy_document.publisher.json

  tags = {
    Project     = var.project_name
    Environment = var.environment
    ManagedBy   = "terraform"
  }
}

resource "aws_iam_user_policy_attachment" "publisher" {
  user       = aws_iam_user.publisher.name
  policy_arn = aws_iam_policy.publisher.arn
}

# ---------------------------------------------------------------------------
# Access key — ID is non-sensitive; secret must be stored in a secrets manager
# ---------------------------------------------------------------------------

resource "aws_iam_access_key" "publisher" {
  user = aws_iam_user.publisher.name
}
