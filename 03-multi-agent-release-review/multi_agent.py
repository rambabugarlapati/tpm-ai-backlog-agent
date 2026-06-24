import os
import time
from google import genai

# 1. Initialize the Gemini client
client = genai.Client()

# Use the highly stable 2.0 flash model
TARGET_MODEL = 'gemini-2.0-flash'

# 2. Read your sample text file
with open("release_notes.txt", "r") as f:
    release_content = f.read()

print(f"🏁 Initiating Multi-Agent Release Review Pipeline using {TARGET_MODEL}...\n")

# --- AGENT 1: The Security Engineer Agent ---
prompt_security = f"You are a strict Cyber Security Architect Agent. Review these release notes for critical security flaws or credential leaks. Be brief:\n\n{release_content}"
response_security = client.models.generate_content(model=TARGET_MODEL, contents=prompt_security)
security_report = response_security.text
print("🛡️ [Security Agent Review Complete]")
print(f"↳ Findings: {security_report.strip()}\n")

# ⏸️ Pause for 10 seconds to protect free-tier API quotas
print("⏳ Pausing for 10 seconds to manage API rate limits...")
time.sleep(10)

# --- AGENT 2: The Product Owner Agent ---
prompt_product = f"You are a Product Owner Agent. Review these release notes to see if user experience or core product metrics are negatively impacted. Be brief:\n\n{release_content}"
response_product = client.models.generate_content(model=TARGET_MODEL, contents=prompt_product)
product_report = response_product.text
print("📦 [Product Agent Review Complete]")
print(f"↳ Findings: {product_report.strip()}\n")

# ⏸️ Pause for 10 seconds to protect free-tier API quotas
print("⏳ Pausing for 10 seconds to manage API rate limits...")
time.sleep(10)

# --- AGENT 3: The TPM Coordinator Agent (The Final Gatekeeper) ---
prompt_tpm = f"""
You are the Lead Technical Program Manager Agent. 
You must review the findings of your technical team and make a final GO or NO-GO deployment decision.

Technical Findings received:
[SECURITY REPORT]: {security_report}
[PRODUCT REPORT]: {product_report}

Provide your final assessment. Structure your answer exactly like this:
1. FINAL DECISION: (GO or NO-GO)
2. RISK MITIGATION STEPS: (What needs to be fixed if it is a NO-GO)
"""

print("🧠 [TPM Coordinator Agent synthesizing reports...]")
final_response = client.models.generate_content(model=TARGET_MODEL, contents=prompt_tpm)

print("\n🚀 FINAL GO/NO-GO REPORT:")
print(final_response.text)
