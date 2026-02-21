from src.video_processing import download_audio
from src.speech_to_text import transcribe_audio
from src.risk_phrase_detector import detect_risk_phrases
from src.disclaimer_checker import check_disclaimer
from src.sentiment_analysis import get_sentiment_score
from src.risk_scoring import calculate_risk_score

youtube_url = input("Enter YouTube URL: ")

print("Downloading audio...")
audio_path = download_audio(youtube_url)

print("Transcribing audio...")
text = transcribe_audio(audio_path)

print("Analyzing content...")

phrases = detect_risk_phrases(text)
disclaimer = check_disclaimer(text)
sentiment = get_sentiment_score(text)

risk = calculate_risk_score(phrases, sentiment, disclaimer)

print("\n--- ANALYSIS RESULT ---")
print("Detected Risk Phrases:", phrases)
print("Disclaimer Present:", disclaimer)
print("Sentiment Score:", sentiment)
print("Final Risk Score:", risk)