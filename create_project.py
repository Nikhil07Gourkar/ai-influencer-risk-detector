import os
import json

# Project structure
folders = [
    "ai_influencer_risk_detector",
    "ai_influencer_risk_detector/src",
    "ai_influencer_risk_detector/data"
]

files = {
    "ai_influencer_risk_detector/src/speech_to_text.py": "",
    "ai_influencer_risk_detector/src/text_cleaning.py": "",
    "ai_influencer_risk_detector/src/risk_phrase_detector.py": "",
    "ai_influencer_risk_detector/src/disclaimer_checker.py": "",
    "ai_influencer_risk_detector/src/sentiment_analysis.py": "",
    "ai_influencer_risk_detector/src/risk_scoring.py": "",
    "ai_influencer_risk_detector/test_script.py": "",
    "ai_influencer_risk_detector/requirements.txt": "",
    "ai_influencer_risk_detector/README.md": "",
    "ai_influencer_risk_detector/data/phrase_library.json": {}
}

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files
for filepath, content in files.items():
    if filepath.endswith(".json"):
        with open(filepath, "w") as f:
            json.dump(content, f, indent=4)
    else:
        with open(filepath, "w") as f:
            f.write(content)

print("Project structure created successfully!")