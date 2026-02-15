# 🎯 PreApply — AI Job Analyzer

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://preapply.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![AI](https://img.shields.io/badge/AI-Google%20Gemini-orange)](https://deepmind.google/technologies/gemini/)
[![Automation](https://img.shields.io/badge/Integration-n8n-red)](https://n8n.io/)

**A tool to analyze CVs against job descriptions using Google Gemini AI.**

**[Try the Live App Here](https://preapply.streamlit.app/)**

This project focuses on using Large Language Models (LLM) to perform gap analysis between a candidate's CV and a target job description. It provides actionable insights, creates tailored content, and includes a demonstration of backend automation using n8n.

## 🚀 Key Features

- **📊 Smart Gap Analysis:** Instantly scores CV relevance and identifies missing skills.
- **✨ CV Improvement:** Rewrites weak points into impactful achievements.
- **✉️ Cover Letter Draft:** Generates a ready-to-send letter based on the analysis.
- **🔒 Privacy-First:** Files are processed in RAM and wiped immediately.

### *Additional Feature (Demo)*
- **🔗 Automation Integration:** A prototype feature that sends structured data (JSON) to an **n8n webhook** to log the application history.
  - *Note: In the live demo, this feature is gated with an admin password.*

## 🛠️ Tech Stack

- **Frontend:** Streamlit
- **AI Engine:** Google Gemini 2.0 Flash
- **Language:** Python
- **Integration:** n8n (Webhook)

## 📦 How to Run Locally

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/albinurrosif/AI-Job-Analyzer-Strategy-Generator.git](https://github.com/albinurrosif/AI-Job-Analyzer-Strategy-Generator.git)
    cd AI-Job-Analyzer-Strategy-Generator
    ```

2.  **Create virtual environment & Install dependencies**
    ```bash
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3.  **Setup Secrets**
    Create `.streamlit/secrets.toml`:

    ```toml
    # Required for the main feature (Analysis)
    GEMINI_API_KEY = "YOUR_GOOGLE_API_KEY"

    # Optional: Only if you want to test the automation feature
    N8N_WEBHOOK_URL = "YOUR_WEBHOOK_URL"
    ADMIN_PASSWORD = "your_password"
    ```

4.  **Run the App**
    ```bash
    streamlit run app.py
    ```

## 👨‍💻 Author

**Albi Nur Rosif**
- [Portfolio](https://albinur.vercel.app/) | [LinkedIn](https://www.linkedin.com/in/albinurrosif/)

---
_© 2026 PreApply._
