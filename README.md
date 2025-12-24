# Test DevSecOps App

This is a test application for the DevSecOps Agent.

## Purpose

This repository is used to test the DevSecOps Agent's deployment capabilities:
- Branch-to-environment mapping
- Deployment commands via comments
- Approval workflows
- Integration test execution

## Structure

- `src/` - Application source code
- `tests/` - Unit and integration tests
- `.github/workflows/` - CI/CD workflows
- `infrastructure/terraform/` - Infrastructure as Code

## Usage

The DevSecOps Agent will interact with this repository to:
1. Deploy to test environments
2. Run integration tests
3. Manage approvals
4. Monitor deployments

## Testing

```bash
# Run unit tests
pytest tests/unit/

# Run integration tests
pytest tests/integration/
```

## Deployment

Deployments are managed by the DevSecOps Agent via PR comments:
- `@devsecops-agent deploy to test`
- `@devsecops-agent run integration tests`
