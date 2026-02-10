import requests
import streamlit as st
from datetime import datetime
import os

def get_webhook_url():
    """Mengambil URL dari Secrets (Cloud) atau Environment (Local)"""
    if "SHEET_WEBHOOK_URL" in st.secrets:
        return st.secrets["SHEET_WEBHOOK_URL"]
    elif "SHEET_WEBHOOK_URL" in os.getenv:
        return os.getenv("SHEET_WEBHOOK_URL")
    return None

def send_to_n8n(company_name, role_name, match_score):
    """
    Fungsi ini tugasnya cuma satu:
    Membungkus data -> Kirim ke N8N -> Lapor Berhasil/Gagal.
    """
    
    url = get_webhook_url()
    
    if not url:
        return False, "⚠️ Configuration Error: Webhook URL not set in secrets."
    
    # N8N needs JSON format
    payload = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "company": company_name,
        "role": role_name,
        "score": match_score,
        "source": "PreApply App"
    }
    
    try:
        response = requests.post(url, json=payload, timeout=5)
        
        if response.status_code == 200:
            return True, "Succefully sent to N8N Tracker"
        else:
            return False, f"Failed to send to N8N Tracker. Status Code: {response.status_code}. Msg: {response.text}"
    except requests.exceptions.RequestException as e:
        return False, f"Error sending to N8N Tracker: {e}"