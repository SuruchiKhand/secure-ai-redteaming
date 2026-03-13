# LLM Security Vulnerability Scanning with Garak

## Overview
This project demonstrates automated LLM vulnerability scanning using NVIDIA Garak, 
an open-source security testing tool for Large Language Models.

## Tools Used
- **Garak v0.14.0** - Automated LLM vulnerability scanner
- **Python 3.11** - Report parsing and statistics extraction
- **Node.js** - Professional Word document generation
- **OpenAI GPT-3.5-turbo** - Target model for security testing

## What I Did
1. Installed and configured Garak on macOS
2. Ran a baseline security scan across 80+ vulnerability categories
3. Ran a targeted prompt injection scan
4. Analyzed and interpreted scan results
5. Generated a professional security audit report

## Key Finding
GPT-3.5-turbo failed **100% of prompt injection tests** (62/62) in the 
`promptinject.HijackHateHumans` category, indicating a critical vulnerability 
where the model can be manipulated to override its instructions in certain contexts.

## Scripts
- `parse_report.py` - Parses raw Garak JSONL output and extracts key statistics
- `generate_report.js` - Generates a formatted Word document security audit report

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

### Generate the report
```bash
python parse_report.py garak_report*.jsonl > parsed_data.json
node generate_report.js
```

## Skills Demonstrated
- LLM security testing and red teaming
- Automated vulnerability scanning
- Security report generation
- Python and Node.js scripting
- AI safety concepts
