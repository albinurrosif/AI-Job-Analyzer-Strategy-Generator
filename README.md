# 🤖 AI Job Analyzer & Strategy Generator

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](LINK_STREAMLIT_CLOUD_ANDA_DISINI)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![Powered by Gemini](https://img.shields.io/badge/AI-Google%20Gemini-orange)](https://deepmind.google/technologies/gemini/)

**An intelligent career consultant tool that helps job seekers tailor their applications perfectly to specific job descriptions.**

This application uses Large Language Models (LLM) to perform gap analysis between a candidate's CV and a target job description, providing actionable feedback, rewritten content, and interview preparation strategies.

## 🚀 Features

* **📄 PDF Resume Parsing:** Extracts text safely from PDF CVs/Resumes.
* **📊 Smart Gap Analysis:** Identifies matching skills and missing requirements with a match score.
* **✨ Magic Bullet Points:** Rewrites weak CV points into impactful, action-oriented statements using the STAR method, tailored to the job's language.
* **✉️ Tailored Cover Letter:** Generates a complete draft based on the candidate's actual strengths and the company's context.
* **🎤 Interview Simulation:** Predicts "Tricky Questions" based on specific CV gaps and provides storytelling-based answers.
* **🌍 Hybrid Language Support:** Explains strategies in Indonesian (for understanding) while generating application assets in the job's native language (English/Indo).
* **🔒 Privacy-First:** Stateless architecture. No data is stored; files are processed in RAM and wiped after the session.

## 🛠️ Tech Stack

* **Framework:** [Streamlit](https://streamlit.io/)
* **LLM Engine:** Google Gemini 2.0 Flash (via `google-genai` SDK)
* **PDF Processing:** `pypdf`
* **Language:** Python

## 📦 How to Run Locally

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

## 💡 How It Works (Prompt Engineering)

The application utilizes a **Chain-of-Thought** prompting strategy with specific constraints:
1.  **Role Playing:** Acts as a "Senior Tech Recruiter".
2.  **Context Injection:** Feeds the parsed PDF and Job Description raw text.
3.  **Strict Formatting:** Uses specific separators to parse the AI's output into clean UI tabs.
4.  **Tone Calibration:** Balances professional criticism with encouraging solutions.

## 🔒 Privacy Policy

This is a portfolio project designed with security in mind:
* **No Database:** User data is not persisted.
* **Ephemeral Processing:** Files are processed in memory and discarded immediately.
* **API Usage:** Data is sent to Google Gemini API solely for analysis during the active session.

## 👨‍💻 Author

**Albi Nur Rosif**
* [Portfolio / Website](https://albinur.vercel.app/)
* [LinkedIn](https://www.linkedin.com/in/albinurrosif/)

---
*If you find this tool useful, please give it a star ⭐!*
