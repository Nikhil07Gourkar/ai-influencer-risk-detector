import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# Example dataset (replace with better data later)
data = {
    "text": [
        "Double your money fast",
        "Secret crypto strategy revealed",
        "Guaranteed profit no risk",
        "Learn stock market basics",
        "How mutual funds work",
        "Beginner investment tutorial"
    ],
    "label": [1, 1, 1, 0, 0, 0]
}

df = pd.DataFrame(data)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["text"])
y = df["label"]

model = LogisticRegression()
model.fit(X, y)

joblib.dump(model, "scam_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("Model trained and saved!")