# Test Environment Infrastructure

This directory contains Terraform configuration for the test environment.

The DevSecOps Agent will manage this infrastructure:
- Spin up environment on demand
- Deploy application
- Destroy environment after testing

## Setup

```bash
cd infrastructure/terraform
terraform init
terraform workspace new test
terraform workspace select test
```

## Usage

The agent will handle:
- `terraform apply` - Spin up environment
- `terraform destroy` - Tear down environment

Manual usage (for testing):
```bash
terraform plan
terraform apply
terraform destroy
```
