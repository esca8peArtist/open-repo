locals {
  bucket_name = "${var.bucket_name_prefix}-${var.environment}"
}

# ---------------------------------------------------------------------------
# S3 bucket
# ---------------------------------------------------------------------------

resource "aws_s3_bucket" "updates" {
  bucket = local.bucket_name

  tags = {
    Project     = var.project_name
    Environment = var.environment
    ManagedBy   = "terraform"
  }
}

# Enforce bucket owner as sole owner — disables ACLs
resource "aws_s3_bucket_ownership_controls" "updates" {
  bucket = aws_s3_bucket.updates.id

  rule {
    object_ownership = "BucketOwnerEnforced"
  }
}

# Block all public access — objects are served exclusively via CloudFront OAC
resource "aws_s3_bucket_public_access_block" "updates" {
  bucket = aws_s3_bucket.updates.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

# Enable versioning so accidental overwrites of manifest.json are recoverable
resource "aws_s3_bucket_versioning" "updates" {
  bucket = aws_s3_bucket.updates.id

  versioning_configuration {
    status = "Enabled"
  }
}

# AES-256 server-side encryption at rest
resource "aws_s3_bucket_server_side_encryption_configuration" "updates" {
  bucket = aws_s3_bucket.updates.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
    bucket_key_enabled = true
  }
}

# Lifecycle: expire non-current object versions after 90 days to control costs.
# Release tarballs are large; old manifest.json versions have no operational value.
resource "aws_s3_bucket_lifecycle_configuration" "updates" {
  bucket = aws_s3_bucket.updates.id

  # Depends on versioning being enabled first
  depends_on = [aws_s3_bucket_versioning.updates]

  rule {
    id     = "expire-noncurrent-versions"
    status = "Enabled"

    noncurrent_version_expiration {
      noncurrent_days = 90
    }

    # Also clean up incomplete multipart uploads (large image tarballs)
    abort_incomplete_multipart_upload {
      days_after_initiation = 7
    }
  }
}
