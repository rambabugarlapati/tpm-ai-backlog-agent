import os
import csv
from google import genai

# 1. Initialize the Gemini client
client = genai.Client()

input_file = "backlog.csv"
output_file = "prioritized_backlog.csv"

print(f"📂 Reading raw tasks from {input_file}...")

# 2. Read tasks from the CSV file
tasks_to_process = []
with open(input_file, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        tasks_to_process.append(row['task_description'])

# 3. Create a structured prompt combining all tasks
formatted_tasks_list = "\n".join([f"- {task}" for task in tasks_to_process])

prompt = f"""
You are an expert Technical Program Manager Agent. 
Analyze the following tasks. 
Categorize each one into High, Medium, or Low priority. 
Assign them to a team (Engineering, Product, or QA). 
Format your output exactly as a CSV table with three columns: Task, Priority, Team.
Do not include markdown formatting or triple backticks in your response. Just the raw CSV text.

Tasks:
{formatted_tasks_list}
"""

print("🤖 Gemini Agent is processing the backlog data...")

# 4. Request the analysis from Gemini
response = client.models.generate_content(
    model='gemini-1.5-flash',
    contents=prompt,
)

# 5. Save the AI's response directly into a new CSV file
with open(output_file, mode='w', encoding='utf-8') as file:
    file.write("Task,Priority,Team\n") # Write headers
    file.write(response.text.strip())

print(f"✅ Success! Saved the prioritized plan to {output_file}")
