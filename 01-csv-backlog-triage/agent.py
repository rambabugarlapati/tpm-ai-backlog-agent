import os
import csv
from google import genai

client = genai.Client()

input_file = "backlog.csv"
output_file = "prioritized_backlog.csv"

print(f"📂 Reading raw tasks from {input_file}...")

tasks_to_process = []
with open(input_file, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        tasks_to_process.append(row['task_description'])

formatted_tasks_list = "\n".join([f"- {task}" for task in tasks_to_process])

prompt = f"""
You are an expert Technical Program Manager Agent. 
Analyze these tasks. Categorize into High, Medium, or Low priority. 
Assign to Engineering, Product, or QA. 
Format output strictly as a CSV table with columns: Task, Priority, Team.
Do not use markdown backticks.

Tasks:
{formatted_tasks_list}
"""

print("🤖 Gemini Agent is processing the backlog data...")
response = client.models.generate_content(
    model='gemini-1.5-flash',
    contents=prompt,
)

with open(output_file, mode='w', encoding='utf-8') as file:
    file.write("Task,Priority,Team\n")
    file.write(response.text.strip())

print(f"✅ Success! Saved results to {output_file}")
