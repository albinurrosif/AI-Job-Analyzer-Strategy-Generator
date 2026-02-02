# 🎯 PreApply — Prepare Before You Apply

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://preapply.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![Powered by Gemini](https://img.shields.io/badge/AI-Google%20Gemini-orange)](https://deepmind.google/technologies/gemini/)

**Your personal AI Career Consultant. Tailor your CV, draft cover letters, and prep for interviews in seconds.**

**[Try the Live App Here](https://preapply.streamlit.app/)**

This application uses Large Language Models (LLM) to perform gap analysis between a candidate's CV and a target job description, providing actionable feedback, rewritten content, and interview preparation strategies.

## 🚀 Features

* **📊 Smart Gap Analysis:** Instant match score with actionable insights on missing skills.
* **✨ Magic Bullet Points:** Rewrites your weak CV points into impactful, STAR-method achievements tailored to the job description.
* **✉️ Tailored Cover Letter:** Drafts a ready-to-send letter in the job's native language (English/Indonesian).
* **🎤 Interview Simulation:** Predicts tricky questions based on *your* specific CV gaps and provides storytelling-based answers.
* **🔒 Privacy-First:** Stateless architecture. Your files are processed in RAM and wiped immediately after the session.

## 🛠️ Tech Stack

* **Frontend:** [Streamlit](https://streamlit.io/)
* **AI Engine:** Google Gemini 2.0 Flash (via `google-genai` SDK)
* **Parser:** `pypdf` for secure PDF text extraction
* **Language:** Python

## 📦 How to Run Locally

If you want to run this application on your own machine:

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/USERNAME_ANDA/NAMA_REPO_ANDA.git](https://github.com/USERNAME_ANDA/NAMA_REPO_ANDA.git)
    cd NAMA_REPO_ANDA
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

4.  **Setup Secrets**
    Create a folder named `.streamlit` in the root directory and add a file named `secrets.toml`:
    ```toml
    # .streamlit/secrets.toml
    GEMINI_API_KEY = "YOUR_GOOGLE_API_KEY_HERE"
    ```
    *(Get your API key from [Google AI Studio](https://aistudio.google.com/))*

5.  **Run the App**
    ```bash
    streamlit run app.py
    ```

## 💡 How It Works

The application utilizes a **Chain-of-Thought** prompting strategy with specific constraints:
1.  **Role Playing:** Acts as a "Senior Tech Recruiter".
2.  **Context Injection:** Feeds the parsed PDF and Job Description raw text to the LLM.
3.  **Strict Formatting:** Uses specific separators to parse the AI's output into clean UI tabs.
4.  **Tone Calibration:** Balances professional criticism with encouraging solutions.

## 👨‍💻 Author

**Albi Nur Rosif**
* [Portfolio / Website](https://albinur.vercel.app/)
* [LinkedIn](https://www.linkedin.com/in/albinurrosif/)

---
*© 2026 PreApply. Automated by Albi Nur Rosif.*