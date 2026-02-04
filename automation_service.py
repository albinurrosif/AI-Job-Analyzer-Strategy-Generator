import requests
import streamlit as st
from datetime import datetime

WEBHOOK_URL = "https://albinurr.app.n8n.cloud/webhook/log-job"

def send_to_n8n(company_name, role_name, match_score):
    """
    Fungsi ini tugasnya cuma satu: 
    Membungkus data -> Kirim ke N8N -> Lapor Berhasil/Gagal.
    """
    
    # N8N needs JSON format
    payload = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "company": company_name,
        "role": role_name,
        "score": match_score,
        "source": "PreApply App"
    }
    
    try:
        response = requests.post(WEBHOOK_URL, json=payload, timeout=5)
        
        if response.status_code == 200:
            return True, "Succefully sent to N8N Tracker"
        else:
            return False, f"Failed to send to N8N Tracker. Status Code: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return False, f"Error sending to N8N Tracker: {e}"