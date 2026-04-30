## Overview
This repository contains hands-on security assessments and red teaming exercises 
from the Secure AI: Red Teaming and Safety Filters course. Each module demonstrates 
practical AI security skills including automated vulnerability scanning, manual 
red teaming, and professional security report generation.

---

## Project 1: LLM Vulnerability Discovery with Automated Tools
`module1-red-teaming-scenarios/ch1-vulnerability-discovery-automated-tools`

**Scenario:** Baseline security scan of GPT-3.5-turbo using NVIDIA Garak 
to understand automated LLM vulnerability testing.

**What I did:**
- Installed and configured Garak v0.14.0 in a conda environment
- Ran automated scans across 80+ vulnerability categories
- Parsed raw JSONL report output using a custom Python script
- Generated a formatted Word security audit report using Node.js

**Key Finding:** GPT-3.5-turbo failed 100% of prompt injection tests 
(62/62) in structured task contexts — same attack succeeded or failed 
depending on the surrounding task, showing context dependency is a 
critical factor in LLM security.

**Tools:** Garak v0.14.0, Python 3.11, Node.js, OpenAI GPT-3.5-turbo

---

## Project 2: ChatAssist Red Team Assessment
`module1-red-teaming-scenarios/chatassist-red-team-assessment`

**Scenario:** Pre-launch security assessment of ChatAssist, a customer 
service chatbot for TechFlow Solutions serving 500,000 customers.

**What I did:**
- Designed 5 manual attack scenarios across key vulnerability categories
  including prompt injection, jailbreaking, data extraction, system 
  prompt exposure, and multi-turn context building
- Ran automated Garak scan across multiple probe categories
- Analyzed results and produced a launch recommendation

**Key Finding:** ANSI escape code exploitation had a 58.82% attack 
success rate — a critical vulnerability that most security teams 
overlook because it targets rendering, not model behavior.

**Recommendation:** Delay launch pending remediation.

**Tools:** Garak v0.14.0, Python 3.11, Node.js, OpenAI GPT-3.5-turbo

---

## Project 3: Safety Filter Implementation for BizAssist HR Chatbot
`module2-content-safety-filters/securechat-safety-filter-assessment`

**Scenario:** Pre-deployment safety filter design and validation for 
BizAssist, an enterprise HR chatbot launching to Fortune 500 clients 
in 72 hours. $15M in contracts depended on passing security audits.

**What I did:**
- Designed a 4-layer safety filter architecture:
  - Layer 1: Input sanitization with 18-term keyword blocklist
  - Layer 2: Semantic analysis with 85% similarity threshold
  - Layer 3: Output filtering with 5 critical checks
  - Layer 4: Behavioral monitoring across conversation turns
- Installed and configured Microsoft PyRIT v0.11.0
- Ran baseline and advanced bypass testing across 14 attack scenarios
- Documented before/after filter performance comparison

**Key Finding:** 0% bypass rate across all 14 scenarios including 
sophisticated multi-turn attacks, Base64 encoding attempts, and CEO 
impersonation — meets the enterprise threshold of less than 5%.

**Recommendation:** Deploy with conditions — weekly PyRIT regression 
testing and false positive monitoring required.

**Tools:** PyRIT v0.11.0, Python 3.11, Node.js, OpenAI GPT-3.5-turbo

---

## Project 4: AnalyzeBot Resilience Assessment
`module3-llm-resilience/analyzebot-resilience-assessment`

**Scenario:** Investigate behavioral drift in AnalyzeBot, DataSecure 
Corporation's AI assistant serving healthcare, financial, and government 
clients after 90 days in production. A Fortune 50 healthcare provider 
with an $8M contract requires quarterly audits with automatic termination 
if security degrades more than 10%.

**What I did:**
- Built a 45-test Promptfoo evaluation suite across 4 vulnerability 
  categories: prompt injection, jailbreaking, data extraction, and 
  system prompt exposure
- Ran baseline assessment establishing a quantitative security posture
- Executed 3 targeted hardening iterations, changing one variable at 
  a time for clear attribution of improvements
- Designed a 4-tier continuous monitoring architecture
- Implemented a CI/CD security gate using GitHub Actions blocking 
  deploys below 85%

**Hardening Results:**

| Iteration | Score | Change |
|-----------|-------|--------|
| Baseline | 33.33% | — |
| Hardening v1 | 84.44% | +51.11pp |
| Hardening v2 | 91.11% | +6.67pp |
| Final | 91.11% | — |

**Key Finding:** A single instruction — "Be as helpful as possible" — 
was the root cause of all behavioral drift. It caused the model to 
comply with social engineering, accept fictional framings as permission 
grants, and treat authority claims as legitimate.

**Recommendation:** Deploy — 91.11% exceeds enterprise threshold of 
90% and contractual floor of 85%.

**Tools:** Promptfoo v0.119, Node.js, GitHub Actions, OpenAI GPT-3.5-turbo

---

## Project 5: FinanceAssist Security Audit
`module3-llm-resilience/financeassist-security-audit`

**Scenario:** Full AI security audit of FinanceAssist, SecureBank's 
AI-powered customer service chatbot, before deployment to 2 million 
customers.

**What I did:**
- Deployed a deliberately vulnerable chatbot and established a 
  quantitative baseline security posture
- Red-teamed using three tools in combination:
  - Garak — automated probe scanning across injection, jailbreak, 
    and data retrieval categories
  - PyRIT — multi-turn adversarial conversation attacks
  - Promptfoo — assertion-based resilience testing
- Designed and implemented a 7-layer safety filter architecture in 
  Python with a YAML configuration file
- Ran 5 hardening iterations measuring security score and false 
  positive rate at each step
- Validated improvements through automated rescanning

**Security Improvement:**

| Metric | Before | After |
|--------|--------|-------|
| Manual security score | 0% | 90% |
| Garak avg attack rate | 41.2% | 3.8% |
| Critical vulnerabilities | 6 | 0 |
| False positive rate | N/A | 0% |
| Promptfoo pass rate | N/A | 83.3% |

**Key Finding:** No single tool provides complete coverage. Garak found 
automated injection vulnerabilities. PyRIT found multi-turn social 
engineering gaps. Promptfoo found encoded injection and academic 
pretexting — two vulnerabilities the other tools missed entirely.

**Recommendation:** Not yet production-ready. Encoded injection and 
sophisticated social engineering represent remaining attack surface 
requiring additional hardening before deployment to 2 million customers.

**Tools:** Garak v0.14.0, PyRIT v0.11.0, Promptfoo v0.121, Python 3.11,
OpenAI GPT-3.5-turbo

---

## How to Reproduce

### Prerequisites
```bash
# Create conda environment
conda create -n redteam python=3.11
conda activate redteam

# Install Python packages
pip install garak pyrit openai python-dotenv presidio-analyzer spacy
python -m spacy download en_core_web_lg

# Install Node.js packages
npm install -g promptfoo
npm install docx

# Set up API key
echo "OPENAI_API_KEY=your-key-here" > .env
```

### Running Each Project
```bash
# Project 1 & 2 — Garak scanning
garak --model_type openai --model_name gpt-3.5-turbo --probes promptinject

# Project 3 — PyRIT filter testing
python pyrit_test.py
python pyrit_test_advanced.py

# Project 4 — Promptfoo resilience testing
promptfoo eval -c promptfooconfig.yaml
promptfoo view

# Project 5 — Full security audit
jupyter notebook security_audit.ipynb
```

---

## Skills Demonstrated

- AI red-teaming using Garak, PyRIT, and Promptfoo
- Safety filter design, implementation, and iterative hardening
- LLM vulnerability assessment across 5 attack categories
- Quantitative security measurement and documentation
- Continuous monitoring pipeline design with CI/CD integration
- Python scripting for filter implementation and report parsing
- Node.js for professional security report generation