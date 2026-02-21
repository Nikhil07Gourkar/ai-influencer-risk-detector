import joblib

model = joblib.load("scam_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

def predict_scam_probability(text):
    X = vectorizer.transform([text])
    prob = model.predict_proba(X)[0][1]
    return round(prob * 100, 2)