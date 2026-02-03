import streamlit as st
from google import genai
from google.genai import types
from google.api_core import exceptions
import pypdf
import re

try:
    from automation_service import send_to_n8n
    AUTOMATION_ACTIVE = True
except ImportError:
    AUTOMATION_ACTIVE = False


# Configuration and UI Setup
def configure_interface():
    """Configure the Streamlit interface for the Job Analyzer AI app."""
    st.set_page_config(page_title="PreApply — Prepare Before You Apply", page_icon="🤖", layout="centered")
    
    # Custom CSS untuk Footer dan Tampilan
    st.markdown("""
        <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: white;
            color: #888;
            text-align: center;
            padding: 10px;
            font-size: 12px;
            border-top: 1px solid #eee;
            z-index: 1000;
        }
        .footer a {
            color: #888;
            text-decoration: none;
            font-weight: bold;
            transition: color 0.3s;
        }
        .footer a:hover {
            color: #007bff !important;
        }
        .block-container {
            padding-bottom: 80px; /* Supaya konten tidak tertutup footer */
        }
        </style>
    """, unsafe_allow_html=True)
    
    st.header("🤖 PreApply")
    st.subheader("Prepare Before You Apply with AI Assistance")
    st.caption("Upload your CV and paste the Job Description. Let AI find the gaps, rewrite your bullet points, and draft your cover letter.")


def get_api_key():
    """Get the API key from Streamlit secrets."""
    try:
        return st.secrets["GEMINI_API_KEY"]
    except FileNotFoundError:
        st.error("Secrets file not found. Please ensure you have a .streamlit/secrets.toml file with the GEMINI_API_KEY.")
        st.stop()
    except KeyError:
        st.error("API key not found. Please set the GEMINI_API_KEY in Streamlit secrets.")
        st.stop()
    except Exception as e:
        st.error(f"An error occurred while loading the API key: {e}")
        st.stop()

# --- HELPERS ---
def extract_text_from_pdf(file):
    """Extract text from a PDF file."""
    try:
        reader = pypdf.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text
    except Exception as e:
        st.error(f"Error reading PDF file: {e}")
        return ""


def reset_page():
    """Reset the Streamlit page to its initial state."""
    st.session_state["role_key"] = ""
    st.session_state["company_key"] = ""
    st.session_state["job_type_key"] = ""
    st.session_state["job_description_key"] = ""
    st.session_state["uploaded_cv_key"] = None
    if "analyze_result" in st.session_state:
        del st.session_state["analyze_result"]
    st.session_state["is_running"] = False

# modal dialog
@st.dialog("ℹ️ Privacy & Security Policy")
def show_privacy_policy():
    st.markdown("""
    **Data Privacy Policy:**
    * This application is stateless.
    * Your CV and Job Description are processed by Google Gemini AI in RAM.
    * No data is saved to any database or disk.
    * All session data is wiped when you refresh or close the tab.
    """)
    st.caption("Automated by Albinurr")


# --- CORE AI LOGIC ---
@st.cache_data(ttl="2h", show_spinner=False)
def analyze_match(api_key, data, cv_text):
    try:
        client = genai.Client(api_key=api_key)

        prompt = f"""
        Role: Expert Tech Recruiter & CV Writer.
        Target Role: {data['role']} at {data['company']} ({data['job_type']}).
    
        JOB DESCRIPTION:
        "{data['job_description']}"
    
        CANDIDATE CV:
        "{cv_text}"
    
        TASK:
        Provide a comprehensive application strategy.
        
        First, VALIDATE the input.
        - Is the Job Description real?
        - Is the CV text sufficient?
        - If the input is GIBBERISH, TOO SHORT, or NONSENSE, output EXACTLY this string: ### INVALID_INPUT ###
    
        If the input is VALID, proceed to provide a comprehensive strategy using the separator '### SECTION_SPLIT ###'.
    
        ⚠️ OUTPUT RULES (STRICT):
        1.  **NO SECTION HEADERS:** JANGAN tulis judul section seperti "[BAGIAN 1]" atau "### Gap Analysis". Langsung tulis isinya saja.
        2.  **SEPARATOR:** Gunakan tepat string '### SECTION_SPLIT ###' sebagai pemisah antar bagian.
    
        ---
    
        [BAGIAN 1: GAP ANALYSIS]
        (Bahasa: INDONESIA)
        1.  **MATCH SCORE:** Tulis skor dalam format HTML ini agar besar dan berwarna hijau:
            `<h2 style='text-align: center; color: #28a745; border: 2px dashed #28a745; padding: 15px; border-radius: 10px; margin-bottom: 20px;'>MATCH SCORE: [MASUKKAN ANGKA]%</h2>`
        2.  Analisis Jujur:
            - ✅ Kekuatan (Match)
            - ⚠️ Kekurangan (Gap)
            - 💡 Strategi Singkat (Solusi menutup gap)
    
        ### SECTION_SPLIT ###
    
        [BAGIAN 2: CV OPTIMIZATION]
        (Bahasa: HYBRID)
        - **Penjelasan & Intro:** Gunakan BAHASA INDONESIA (agar saya paham konteksnya).
        - **Keywords & Contoh Kalimat (Rewrites):** Gunakan BAHASA YANG SAMA DENGAN JOB DESC (Inggris/Indo).
    
        Isi:
        1. Daftar ATS Keywords yang wajib ada.
        2. **MAGIC BULLET POINTS:** Pilih 3 poin terlemah di CV saya, berikan kritik singkat (Indo), lalu tulis ulang kalimatnya (Bahasa Lowongan) dengan format 'Action Verb + Result'.
    
        ### SECTION_SPLIT ###
    
        [BAGIAN 3: COVER LETTER]
        (Bahasa: SAMA DENGAN JOB DESC - Inggris/Indo)
        - Tulis surat lamaran lengkap.
        - JANGAN gunakan bolding/markdown headers (judul). Tulis sebagai paragraf polos agar mudah di-copy paste ke email.
    
        ### SECTION_SPLIT ###
    
        [BAGIAN 4: INTERVIEW PREP]
        (Bahasa: INDONESIA - Human Touch)
        - Berikan 2 pertanyaan paling wajar muncul dan 2 pertanyaan jebakan yang paling mungkin muncul.
        - Untuk setiap pertanyaan, berikan "Contoh Jawaban" dengan gaya bercerita (Storytelling) menggunakan pengalaman nyata yang ADA DI CV SAYA (Gunakan metode STAR).
        """
    
        with st.spinner("🤖 AI is analyzing your profile..."):
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
        )
        return response.text
    except exceptions.ResourceExhausted:
        return "⚠️ QUOTA_EXCEEDED"
    except Exception as e:
        return f"Sorry, an error occurred while processing your request: {e}"



######################################################################################## main ############################################################################################


def main():
    """ Main function to run the Streamlit app."""

    configure_interface()
    api_key = get_api_key()
    
    if "is_running" not in st.session_state:
        st.session_state.is_running = False
    
    def start_analysis():
        st.session_state.is_running = True
    

    # Streamlit input fields
    role = st.text_input("Enter the Job Role Description", placeholder="e.g., Software Engineer, Data Analyst, etc.", key="role_key")
    uploaded_cv = st.file_uploader("Upload Your CV (PDF or TXT)", type=["pdf", "txt"], key="uploaded_cv_key")
    st.caption("🔒 *Privacy Note: Files are processed in memory and not stored.*")
    col1, col2 = st.columns(2)
    with col1:
        company = st.text_input("Company Name", placeholder="e.g., Google (Tech), BCA (Finance)", key="company_key")

    with col2:
        job_type = st.selectbox("Select Job Type", ["Full-time", "Part-time", "Internship", "Contract", "Freelance", "Non-specified"] , key="job_type_key")
    job_description = st.text_area("Enter/Paste the Job Description", height=230, placeholder="e.g., Responsibilities, Requirements, etc." , key="job_description_key")

    col_btn1, col_btn2, col_btn3 = st.columns([2, 1, 1])
    with col_btn1:
        analyze_button = st.button("Analyze", type="primary", use_container_width=True, disabled=st.session_state.is_running, on_click=start_analysis)
    with col_btn2:
        clear_button = st.button("Reset", type="secondary", use_container_width=True, on_click=reset_page)
    with col_btn3:
        st.empty()
    
    if st.session_state.is_running:
        st.session_state["is_running"] = True
        if not role or not company or not job_type or not job_description or not uploaded_cv:
            st.warning("⚠️ Please fill in all the required fields.")
            st.session_state["is_running"] = False
        else:
            # Extract CV text
            cv_text = extract_text_from_pdf(uploaded_cv) if uploaded_cv.type == "application/pdf" else str(uploaded_cv.read(), "utf-8")

            if cv_text:
                # Prepare user data
                user_data = {
                    "role": role,
                    "company": company,
                    "job_type": job_type,
                    "job_description": job_description
                }
                # Analyze
                analyze_result = analyze_match(api_key, user_data, cv_text)

                if analyze_result is None:
                    st.warning("⚠️ AI API quota exceeded. Please try again tomorrow.")
                st.session_state["analyze_result"] = analyze_result
                st.session_state["is_running"] = False
                st.rerun()

    if "analyze_result" in st.session_state:
        result = st.session_state["analyze_result"]
        
        if result == "⚠️ QUOTA_EXCEEDED":
            st.error("⚠️ AI API quota exceeded. Please try again tomorrow.")
        elif result == "### INVALID_INPUT ###":
            st.error("⚠️ Invalid input detected. Please ensure your Job Description and CV are valid and sufficient.")
        elif result.startswith("Sorry, an error occurred"):
            st.error(result)
        else:
            st.divider()
        
            try:
                parts = result.split("### SECTION_SPLIT ###")
            
                tab1,tab2,tab3,tab4 = st.tabs(["📊 Analysis & Gaps", 
                    "✨ CV Improvements", 
                    "✉️ Cover Letter", 
                    "❓ Interview Prep"])
            
                with tab1:
                    st.markdown("### 📊 Analysis & Gaps")
                    st.markdown(parts[0], unsafe_allow_html=True)
                with tab2:
                    st.markdown("### ✨ Optimized Content")
                    st.info("Copy these bullet points to update your CV.")
                    if len(parts) > 1:
                        st.markdown(parts[1])
                with tab3:
                    st.markdown("### ✉️ Draft Application")
                    st.info("Copy this cover letter to use in your application.")
                    if len(parts) > 2:
                        clean_letter = parts[2].strip()
                        st.code(clean_letter, language="text")
                with tab4:
                    st.markdown("### ❓ Interview Preparation")
                    st.info("Practice these questions and answers to ace your interview.")
                    if len(parts) > 3:
                        st.markdown(parts[3])
            
                st.divider()
                
                if AUTOMATION_ACTIVE:
                    st.markdown("### 🚀 Aplication Pipeline Tracker")
                    st.caption("Satisfied with the result? Send to Job Apllication Tracker")
                    
                    col1, col2 = st.columns([1,2])
                    
                    with col1:
                        if st.button("Save to Tracker"):
                            
                            with st.spinner("Sending data to N8N..."):
                                # get ai result
                                full_text = st.session_state.get("analyze_result","")
                                
                                # search the anchor word with regex
                                # Cari teks yang polanya: "MATCH SCORE:" diikuti spasi, lalu Angka
                                # r"MATCH SCORE:\s*(\d+)%"
                                # \s* = spasi (boleh ada boleh tidak)
                                # (\d+) = ambil angkanya
                                match = re.search(r"MATCH SCORE:\s*(\d+)%", full_text)
                                
                                if match:
                                    match_score = match.group(1) + "%"
                                else:
                                    match_score = "Analyzed"

                                success, message = send_to_n8n(company, role, match_score)
                                if success:
                                    st.success(f"Data sent to N8N Tracker!")
                                    st.balloons()
                                else:
                                    st.error(message)

            except Exception as e:
                st.error(f"An error occurred while processing the AI response: {e}")
                st.markdown(st.session_state["analyze_result"])
    
    # Privacy & Security Info
    st.markdown("---")
    f_col1, f_col2, f_col3 = st.columns([1,2,1])
    with f_col2:
        st.markdown("""
                    <div style='text-align: center; color: #888; font-size: 14px;'>
                    © 2026 PreApply • Automated by
                    <a href="https://albinur.vercel.app/" target="_blank">Albinurr 🤖</a>
                    </div>
                    """, unsafe_allow_html=True)
        sub_col1, sub_col2, sub_col3 = st.columns([1,2,1])
        with sub_col2:
            if st.button("🔒 Privacy & Security", type="tertiary", use_container_width=True):
                show_privacy_policy()

if __name__ == "__main__":
    main()