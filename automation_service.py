import requests
import streamlit as st
from datetime import datetime

WEBHOOK_URL = "https://albinurr.app.n8n.cloud/webhook/log-job"

def send_to_n8n(company_name, role_name, match_score):
    """
    Fungsi ini tugasnya cuma satu: 
    Membungkus data -> Kirim ke N8N -> Lapor Berhasil/Gagal.
    """
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Content-Type": "application/json"
    }
    
    # N8N needs JSON format
    payload = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "company": company_name,
        "role": role_name,
        "score": match_score,
        "source": "PreApply App"
    }
    
    st.write(f"**1. URL Target:** `{WEBHOOK_URL}`")
    st.write(f"**2. Data yang dikirim:** Company={company_name}, Role={role_name}, Score={match_score}")
    
    try:
        response = requests.post(WEBHOOK_URL, json=payload, headers=headers, timeout=5)
        
        # 3. CEK STATUS CODE
        st.write(f"**3. HTTP Status Code:** `{response.status_code}`")
                                    
        # 4. CEK RESPON BODY (INI KUNCINYA!)
        # N8N biasanya memberi tahu KENAPA dia menolak (misal: "workflow not active")
        st.write("**4. Response Text dari N8N:**")
        st.code(response.text)
        
        if response.status_code == 200:
            return True, "Succefully sent to N8N Tracker"
        else:
            return False, f"Failed to send to N8N Tracker. Status Code: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return False, f"Error sending to N8N Tracker: {e}"