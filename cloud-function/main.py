import base64
import json
import requests
import os

SLACK_WEBHOOK_URL = os.environ['SLACK_WEBHOOK_URL']

def notify_slack(event, context):
    data = base64.b64decode(event['data']).decode('utf-8')
    message = f"✅ App Engine Deployment Success: {data}"

    payload = {
        "text": message,
        "username": "GCP Notifier",
        "icon_emoji": ":rocket:"
    }

    response = requests.post(SLACK_WEBHOOK_URL, json=payload)
    print("Slack response:", response.status_code)
 
