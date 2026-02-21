import requests
import streamlit as st

st.title("🚨 AI Influencer Scam Detector")

youtube_url = st.text_input("Paste YouTube Video URL")

if st.button("Analyze Video"):
    if youtube_url:
        response = requests.post(
            "http://127.0.0.1:8000/predict-youtube",
            json={"url": youtube_url}
        )

        data = response.json()

        if "error" in data:
            st.error(data["error"])
        else:
            st.success(f"Risk Level: {data['risk_level']}")
            st.metric("Scam Probability", f"{round(data['scam_probability']*100,2)}%")