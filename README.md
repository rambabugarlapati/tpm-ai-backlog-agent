# TPM AI Automation Suite 🤖💼

A collection of production-inspired Python prototypes demonstrating how AI Agents can automate Technical Program Management workflows, optimize engineering velocity, and handle system orchestration.

## 📁 Repository Structure

### 📂 [01-csv-backlog-triage](./agent.py)
* **What it does**: Reads raw project tasks from a CSV file and uses Gemini to categorize priority and assign cross-functional engineering teams.
* **Core Concepts**: Data I/O, Prompt Engineering, Cost-efficient token utilization.

### 📂 [02-jira-slack-orchestrator](./02-jira-slack-orchestrator)
* **What it does**: Ingests unstructured customer incident reports, performs an automated technical triage, and generates validated JSON payloads for Jira ticket creation and executive Slack alerts.
* **Core Concepts**: Structured JSON Outputs, Automated Incident Routing, Mock API Integration.

## 🛠️ Tech Stack & Prerequisites
* **Language**: Python 3.x
* **Orchestration**: Google GenAI SDK (`gemini-1.5-flash`)
* **Environment Variables**: Managed securely via system configurations.
