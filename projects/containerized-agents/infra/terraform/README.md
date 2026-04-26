# AgentCore Update Server — Terraform Infrastructure

Provisions the AWS infrastructure that backs the AgentCore update server:
an S3 bucket (private, versioned, encrypted) served through a CloudFront
distribution, plus a least-privilege IAM user for `publish_release.py`.

## Architecture

```
publish_release.py
  │
  ├─ s3:PutObject ──► S3 bucket (agentcore-updates-<env>)
  │                       private, AES-256, versioned
  │                       <─── served via ───►  CloudFront distribution
  │                                               HTTPS only, TLSv1.2_2021
  │                                               PriceClass_100
  └─ cloudfront:CreateInvalidation ──► invalidates /manifest.json
```

Objects in S3 are never publicly accessible. CloudFront uses Origin Access
Control (OAC / SigV4) to authenticate requests to the bucket.

## Prerequisites

- Terraform >= 1.7
- AWS credentials with permissions to create S3, CloudFront, and IAM resources
- An AWS account where CloudFront is enabled

## Quick Start

### 1. Configure variables

```bash
cd infra/terraform
cp terraform.tfvars.example terraform.tfvars
# Edit terraform.tfvars — set environment = "staging" or "prod"
```

### 2. Configure remote state (recommended)

Create an S3 bucket and DynamoDB table for state locking, then add a
`backend.tf` file:

```hcl
# infra/terraform/backend.tf  (do not commit — state may contain secrets)
terraform {
  backend "s3" {
    bucket         = "my-terraform-state-bucket"
    key            = "agentcore/update-server/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "terraform-state-lock"
    encrypt        = true
  }
}
```

### 3. Initialise

```bash
terraform init
```

### 4. Preview changes

```bash
terraform plan -var-file=terraform.tfvars
```

### 5. Apply

```bash
terraform apply -var-file=terraform.tfvars
```

Terraform will print all outputs on completion. Capture the sensitive
`publisher_secret_key` output now — it cannot be retrieved again without
recreating the access key:

```bash
terraform output -json | jq '{
  bucket:         .bucket_name.value,
  distribution:   .cloudfront_distribution_id.value,
  access_key_id:  .publisher_access_key_id.value,
  secret_key:     .publisher_secret_key.value
}'
```

## Configuring publish_release.py

Set the following environment variables (e.g. in GitHub Actions secrets or
your CI/CD vault) using the Terraform outputs:

| Environment variable       | Terraform output                  |
|----------------------------|-----------------------------------|
| `AWS_ACCESS_KEY_ID`        | `publisher_access_key_id`         |
| `AWS_SECRET_ACCESS_KEY`    | `publisher_secret_key` (sensitive)|
| `AWS_REGION`               | value of `var.aws_region`         |
| `S3_BUCKET`                | `bucket_name`                     |
| `CLOUDFRONT_DISTRIBUTION`  | `cloudfront_distribution_id`      |
| `UPDATE_SIGNING_KEY`       | 32-byte Ed25519 key (hex) — generated separately, stored in secrets manager |

Example publish command:

```bash
python update_server/publish_release.py \
  --version 1.2.0 \
  --changelog "## v1.2.0\n- Bug fixes" \
  --agentcore-image dist/agentcore-1.2.0.tar.gz \
  --wizard-image dist/wizard-1.2.0.tar.gz
```

## Custom Domain

To use a custom domain (e.g. `updates.agentcore.io`) instead of the default
`*.cloudfront.net` domain:

1. Request an ACM certificate in `us-east-1` for your domain.
2. Add to `cloudfront.tf` inside the `aws_cloudfront_distribution` resource:

```hcl
aliases = ["updates.agentcore.io"]

viewer_certificate {
  acm_certificate_arn      = "arn:aws:acm:us-east-1:123456789012:certificate/..."
  ssl_support_method       = "sni-only"
  minimum_protocol_version = "TLSv1.2_2021"
}
```

3. Create a DNS CNAME for `updates.agentcore.io` → `cloudfront_domain` output.

## Teardown

```bash
terraform destroy -var-file=terraform.tfvars
```

Note: The S3 bucket must be empty before it can be destroyed. Either empty it
manually or set `force_destroy = true` on `aws_s3_bucket.updates` before
running destroy.

## Resource Summary

| Resource | Name pattern |
|---|---|
| S3 bucket | `<bucket_name_prefix>-<environment>` |
| CloudFront distribution | (assigned by AWS) |
| CloudFront OAC | `agentcore-updates-oac-<environment>` |
| IAM user | `agentcore-update-publisher-<environment>` |
| IAM policy | `agentcore-update-publisher-policy-<environment>` |
