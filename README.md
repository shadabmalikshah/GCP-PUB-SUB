# GCP App Engine Pub/Sub Slack Notifier PoC

## Structure:
- app/: Simple Hello World app for App Engine
- cloud-function/: Slack Notifier triggered by Pub/Sub
- .github/workflows/: GitHub Actions CI/CD workflow

## Steps:
1. Deploy the Cloud Function (set SLACK_WEBHOOK_URL)
2. Push to GitHub main branch
3. GitHub Action deploys App Engine, triggers Pub/Sub
4. Cloud Function posts a message to Slack
