import os
from google import genai

# 1. Initialize the Gemini client
# It looks for an environment variable named GEMINI_API_KEY
client = genai.Client()

# 2. Define the raw TPM data
messy_tasks = """
- Fix the login bug reported by QA. It is blocking the release.
- Update the onboarding documentation for new hires.
- Prepare the Q3 steering committee slide deck. Due tomorrow.
- Investigate why the database latency spiked at 2 AM.
"""

# 3. Design the prompt for your agent
prompt = f"""
You are an expert Technical Program Manager Agent. 
Analyze the following tasks. 
Categorize each one into High, Medium, or Low priority. 
Assign them to a team (Engineering, Product, or QA). 
Respond only in a clean bulleted list.

Tasks:
{messy_tasks}
"""

print("🤖 TPM Agent is analyzing the backlog...")

# 4. Call the Gemini 1.5 Flash model
response = client.models.generate_content(
    model='gemini-1.5-flash',
    contents=prompt,
)

# 5. Print the formatted backlog
print("\n📋 Optimized Backlog:")
print(response.text)


Add initial TPM agent script
