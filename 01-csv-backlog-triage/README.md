# TPM AI Backlog Agent 🤖

A lightweight Python prototype demonstrating how an AI Technical Program Manager (TPM) Agent can automate backlog grooming, task triage, and cross-functional team assignments.

## 🚀 Overview
This project showcases prompt engineering and automated text processing using the Google Gemini API. It takes a raw, unstructured list of project issues and instantly returns a prioritized, team-assigned action plan.

## 🛠️ Tech Stack & Concepts Demonstrated
* **LLM Orchestration**: Built using the official Google GenAI SDK.
* **Model**: Gemini 1.5 Flash (chosen for low latency and high cost-efficiency).
* **TPM Automation**: Demonstrates how to automate core program management workflows like task prioritization and ticket routing.

## 📋 How It Works
The script sends a messy backlog to the Gemini model with specific routing instructions.

### Input Data:
* Fix the login bug reported by QA. It is blocking the release.
* Update the onboarding documentation for new hires.
* Prepare the Q3 steering committee slide deck. Due tomorrow.
* Investigate why the database latency spiked at 2 AM.

### Expected Agent Output:
* **Fix the login bug**: High Priority | Engineering
* **Prepare the Q3 slide deck**: High Priority | Product
* **Investigate database latency**: Medium Priority | Engineering
* **Update onboarding docs**: Low Priority | Product

## 💻 How to Run Locally
1. Clone this repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Set your API Key: `export GEMINI_API_KEY="your_api_key"`
4. Run the script: `python agent.py`

