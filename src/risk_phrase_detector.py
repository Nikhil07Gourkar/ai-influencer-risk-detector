import json

def load_phrase_library():
    with open("data/phrase_library.json", "r") as f:
        return json.load(f)

def detect_risk_phrases(text):
    library = load_phrase_library()
    phrases = library["high_risk_phrases"]

    found_phrases = []

    for phrase in phrases:
        if phrase in text.lower():
            found_phrases.append(phrase)

    return found_phrases