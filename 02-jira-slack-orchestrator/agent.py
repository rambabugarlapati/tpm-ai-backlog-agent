import os
import json
from google import genai

# 1. Initialize the Gemini client
client = genai.Client()

# 2. Simulate an incoming raw production incident ticket
raw_incident = """
From: customer_success@company.com
Subject: Checkout Page Broken!!
Body: Urgent! Users are reporting that when they click the 'Pay Now' button, 
the spinner just spins forever and they get a blank white screen. 
This is happening on both Chrome and Safari. We are losing sales. Please fix ASAP!
"""

# 3. Create a highly structured prompt forcing a JSON format output
prompt = f"""
You are an expert AI Technical Program Manager Agent. 
Analyze the following raw customer incident and generate two specific API payloads.

1. A Jira Ticket Payload:
   - "title": Clean, professional summary.
   - "description": Detailed technical breakdown based on the incident report.
   - "priority": High, Medium, or Low.
   - "component": The engineering area affected (e.g., Frontend, Backend, Database).

2. A Slack Alert Payload:
   - "channel": Always "#incident-response".
   - "text": A brief, urgent summary message tailored for executive leadership.

You MUST respond strictly in valid JSON format with two root keys: "jira_payload" and "slack_payload". 
Do not include markdown code block formatting (like ```json). Just the raw JSON.

Incident:
{raw_incident}
"""

print("🔍 Analyzing incoming production incident...")

# 4. Request the structured response from Gemini
response = client.models.generate_content(
    model='gemini-1.5-flash',
    contents=prompt,
)

# 5. Parse and pretty-print the result to simulate sending it to APIs
try:
    # Convert the text string from Gemini into a real Python dictionary
    payloads = json.loads(response.text.strip())
    
    print("\n🎫 [SIMULATED] Successfully created Jira Ticket Payload:")
    print(json.dumps(payloads["jira_payload"], indent=2))
    
    print("\n💬 [SIMULATED] Successfully posted to Slack API:")
    print(json.dumps(payloads["slack_payload"], indent=2))
    
except Exception as e:
    print(f"❌ Error parsing JSON payload: {e}")
    print("Raw output from AI:")
    print(response.text)
