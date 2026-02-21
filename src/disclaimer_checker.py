import json

def check_disclaimer(text):
    with open("data/phrase_library.json", "r") as f:
        library = json.load(f)

    disclaimers = library["disclaimers"]

    for phrase in disclaimers:
        if phrase in text.lower():
            return True

    return False