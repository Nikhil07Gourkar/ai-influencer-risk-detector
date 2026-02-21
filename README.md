# 🚨 AI Influencer Risk Detector
### Detect Scam Probability in Finance & Crypto YouTube Videos Using NLP & Machine Learning

---

## 📌 Overview

AI Influencer Risk Detector is a Machine Learning powered web application that analyzes finance and cryptocurrency-related YouTube video transcripts to detect potential scam content.

The system extracts transcripts, performs NLP-based feature engineering, and predicts scam probability using trained ML models.

---

## 🎯 Problem Statement

With the rise of crypto and finance influencers, many fraudulent schemes are promoted through YouTube videos.  
This project aims to:

- Detect potential scam signals
- Quantify scam probability
- Classify risk level (Low / Medium / High)
- Provide explainable risk analysis

---

## 🏗️ System Architecture

User Input (YouTube URL)  
⬇  
Transcript Extraction (YouTube Transcript API)  
⬇  
Text Preprocessing (NLP Pipeline)  
⬇  
Feature Engineering  
⬇  
Machine Learning Model  
⬇  
Risk Probability Output  

---

## 🧠 Machine Learning Pipeline

- Text Cleaning
- Tokenization
- Stopword Removal
- Sentiment Analysis (VADER)
- NLP Processing (spaCy)
- Feature Extraction (TF-IDF / Custom Features)
- Classification Model (Scikit-learn)

---

## 📊 Features

✔ Scam Probability Score  
✔ Risk Level Classification  
✔ YouTube Transcript Extraction  
✔ NLP-based Sentiment Analysis  
✔ ML-based Classification  
✔ Streamlit Dashboard Interface  

---

## 🛠️ Tech Stack

- Python
- FastAPI
- Streamlit
- Scikit-learn
- spaCy
- NLTK
- VADER Sentiment
- YouTube Transcript API
