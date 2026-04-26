# ---------------------------------------------------------------------------
# S3
# ---------------------------------------------------------------------------

output "bucket_name" {
  description = "Name of the S3 bucket serving update artifacts. Set as S3_BUCKET env var for publish_release.py."
  value       = aws_s3_bucket.updates.bucket
}

output "bucket_arn" {
  description = "ARN of the S3 updates bucket."
  value       = aws_s3_bucket.updates.arn
}

# ---------------------------------------------------------------------------
# CloudFront
# ---------------------------------------------------------------------------

output "cloudfront_domain" {
  description = "CloudFront distribution domain name (e.g. d1abc.cloudfront.net). Point your custom CNAME here."
  value       = aws_cloudfront_distribution.updates.domain_name
}

output "cloudfront_distribution_id" {
  description = "CloudFront distribution ID. Set as CLOUDFRONT_DISTRIBUTION env var for publish_release.py."
  value       = aws_cloudfront_distribution.updates.id
}

# ---------------------------------------------------------------------------
# IAM publisher credentials
# ---------------------------------------------------------------------------

output "publisher_iam_user_arn" {
  description = "ARN of the IAM user used by publish_release.py."
  value       = aws_iam_user.publisher.arn
}

output "publisher_access_key_id" {
  description = "AWS access key ID for the publisher IAM user. Set as AWS_ACCESS_KEY_ID env var."
  value       = aws_iam_access_key.publisher.id
}

output "publisher_secret_key" {
  description = "AWS secret access key for the publisher IAM user. Set as AWS_SECRET_ACCESS_KEY env var. Store in a secrets manager — never commit this value."
  value       = aws_iam_access_key.publisher.secret
  sensitive   = true
}
