from fastapi import FastAPI
from pydantic import BaseModel
from youtube_transcript_api import YouTubeTranscriptApi
from src.classifier import predict_scam_probability
import re

app = FastAPI()

class YouTubeRequest(BaseModel):
    url: str

def extract_video_id(url):
    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(pattern, url)
    return match.group(1) if match else None

@app.get("/")
def root():
    return {"message": "AI Influencer Risk Detector API Running"}

@app.post("/predict-youtube")
def predict_from_youtube(request: YouTubeRequest):
    video_id = extract_video_id(request.url)
    
    if not video_id:
        return {"error": "Invalid YouTube URL"}

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        full_text = " ".join([t["text"] for t in transcript])
    except:
        return {"error": "Transcript not available"}

    probability = predict_scam_probability(full_text)

    return {
        "video_id": video_id,
        "scam_probability": float(probability),
        "risk_level": "High" if probability > 0.7 else "Medium" if probability > 0.4 else "Low"
    }