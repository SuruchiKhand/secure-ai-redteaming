# AI Security: Red Teaming and LLM Vulnerability Assessment

## Overview
This repository contains hands-on security assessments and red teaming exercises 
from the Secure AI: Red Teaming and Safety Filters course. Each module demonstrates 
practical AI security skills including automated vulnerability scanning, manual 
red teaming, and professional security report generation.

## Repository Structure
```
secure-ai-redteaming/
    └── module1-red-teaming-scenarios/
        └── ch1-vulnerability-discovery-automated-tools/
            ├── parse_report.py
            ├── generate_report.js
            ├── parsed_data.json
            ├── package.json
            ├── package-lock.json
            └── LLM_Security_Audit_Report.docx
        └── chatassist-red-team-assessment/
            ├── generate_chatassist_report.js
            └── ChatAssist_Red_Team_Assessment.docx
    └── PORTFOLIO.md
    └── README.md
```

## Module 1: Red Teaming Scenarios for LLM Vulnerabilities

### Chapter: Hands-on Vulnerability Discovery with Automated Tools
Automated LLM vulnerability scanning using NVIDIA Garak against OpenAI GPT-3.5-turbo.

**Key Finding:** GPT-3.5-turbo failed 100% of prompt injection tests (62/62) in the
`promptinject.HijackHateHumans` category.

**Scripts:**
- `parse_report.py` — Parses raw Garak JSONL output and extracts key statistics
- `generate_report.js` — Generates a formatted Word document security audit report

### Graded Assignment: Red Team Assessment of ChatAssist Customer Service Bot
Pre-launch red team security assessment of ChatAssist, a customer service chatbot 
for TechFlow Solutions serving 500,000 customers.

**Key Finding:** ANSI escape code exploitation had a critical attack success rate 
of 58.82%. Launch was recommended to be delayed pending security fixes.

**Scripts:**
- `generate_chatassist_report.js` — Generates the full red team assessment report

## Tools Used
- **Garak v0.14.0** — Automated LLM vulnerability scanner
- **Python 3.11** — Report parsing and statistics extraction
- **Node.js** — Professional Word document generation
- **OpenAI GPT-3.5-turbo** — Target model for security testing

## How to Run

### Prerequisites
- Python 3.10+
- Node.js
- OpenAI API key

### Installation
```bash
pip install garak
npm install docx
```

### Run a baseline scan
```bash
export OPENAI_API_KEY="your-key-here"
garak --model_type openai --model_name gpt-3.5-turbo
```

### Run a targeted prompt injection scan
```bash
garak --model_type openai --model_name gpt-3.5-turbo --probes promptinject --report_prefix garak_report
```

### Generate the LLM Security Audit Report
```bash
python parse_report.py garak_report*.jsonl > parsed_data.json
node generate_report.js
```

### Generate the ChatAssist Red Team Assessment Report
```bash
cd module1-red-teaming-scenarios/chatassist-red-team-assessment
npm install docx
node generate_chatassist_report.js
```

## Skills Demonstrated
- LLM security testing and red teaming
- Manual attack scenario design across 5 vulnerability categories
- Automated vulnerability scanning with Garak
- Security report generation and documentation
- Python and Node.js scripting
- AI safety concepts and remediation recommendations
- SSH key setup and GitHub version control