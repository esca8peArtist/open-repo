variable "aws_region" {
  description = "AWS region for the primary provider (S3 bucket, IAM resources)."
  type        = string
  default     = "us-east-1"
}

variable "environment" {
  description = "Deployment environment. Must be 'staging' or 'prod'."
  type        = string

  validation {
    condition     = contains(["staging", "prod"], var.environment)
    error_message = "environment must be 'staging' or 'prod'."
  }
}

variable "bucket_name_prefix" {
  description = "Prefix for the S3 bucket name. The final name will be '<prefix>-<environment>'."
  type        = string
  default     = "agentcore-updates"
}

variable "project_name" {
  description = "Project name used for resource tagging."
  type        = string
  default     = "agentcore"
}
