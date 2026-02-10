# 🎯 PreApply — Prepare Before You Apply

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://preapply.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![AI](https://img.shields.io/badge/AI-Google%20Gemini-orange)](https://deepmind.google/technologies/gemini/)
[![Automation](https://img.shields.io/badge/Automation-n8n-red)](https://n8n.io/)

**Your personal AI Career Consultant & Automated Job Tracker.**
**Tailor your CV, draft cover letters, and log applications to Google Sheets in seconds.**

**[Try the Live App Here](https://preapply.streamlit.app/)**

This application uses Large Language Models (LLM) to perform gap analysis between a candidate's CV and a target job description, while streamlining the application tracking process via n8n automation workflows.

## 🚀 Features

- **📊 Smart Gap Analysis:** Instant match score with actionable insights on missing skills.
- **✨ Magic Bullet Points:** Rewrites your weak CV points into impactful, STAR-method achievements.
- **✉️ Tailored Cover Letter:** Drafts a ready-to-send letter in the job's native language.
- **🤖 Automated Pipeline Tracker (New!):**
  - Integrated with **n8n** workflows via Webhook.
  - One-click save to **Google Sheets** for real-time application tracking.
  - _Note: Protected by Admin Gate for privacy._
- **🔒 Privacy-First:** Stateless architecture. Files are processed in RAM and wiped immediately.

## 🛠️ Tech Stack

- **Frontend:** [Streamlit](https://streamlit.io/)
- **AI Engine:** Google Gemini 2.5 Flash
- **Automation:** [n8n](https://n8n.io/) (Webhook & Google Sheets Node)
- **Database:** Google Sheets (via API)
- **Language:** Python

## 📦 How to Run Locally

If you want to run this application (and use the tracker feature) on your own machine:

1.  **Clone the repository**

    ```bash
    git clone [https://github.com/albinurrosif/AI-Job-Analyzer-Strategy-Generator.git](https://github.com/albinurrosif/AI-Job-Analyzer-Strategy-Generator.git)
    cd AI-Job-Analyzer-Strategy-Generator
    ```

2.  **Create a virtual environment**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

3.  **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Setup Secrets (Crucial)**
    Create a folder named `.streamlit` in the root directory and add a file named `secrets.toml`.

    You need to configure your AI Key and (Optional) Automation Webhook:

    ```toml
    # .streamlit/secrets.toml

    # 1. Required for AI Features
    GEMINI_API_KEY = "YOUR_GOOGLE_API_KEY"

    # 2. Optional: For Job Tracker Feature (n8n / Zapier)
    N8N_WEBHOOK_URL = "YOUR_WEBHOOK_URL_HERE"

    # 3. Optional: Secure the tracker feature with a password
    ADMIN_PASSWORD = "your_secret_password"
    ```

5.  **Run the App**
    ```bash
    streamlit run app.py
    ```

## 💡 How It Works

### 1. The AI Core (Gemini)

The app uses a **Chain-of-Thought** prompting strategy to act as a "Expert Recruiter". It validates the input, performs a gap analysis, and generates tailored content using strict formatting rules.

### 2. The Automation Engine (n8n)

When the "Save to Tracker" button is clicked (Admin Mode):

1.  **Python** extracts the `Company`, `Role`, and `Match Score`.
2.  Data is sent as a JSON payload to an **n8n Webhook**.
3.  **n8n Workflow** captures the data and appends a new row to a specific **Google Sheet**.
4.  Success response is sent back to the Streamlit UI.

## 👨‍💻 Author

**Albi Nur Rosif**

- [Portfolio / Website](https://albinur.vercel.app/)
- [LinkedIn](https://www.linkedin.com/in/albinurrosif/)

---

_© 2026 PreApply. Automated by Albi Nur Rosif._
