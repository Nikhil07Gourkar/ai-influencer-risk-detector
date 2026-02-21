def generate_explanation(risk_score, phrases, sentiment, scam_prob):
    reasons = []

    if scam_prob > 70:
        reasons.append("High scam probability detected by AI classifier")

    if len(phrases) > 0:
        reasons.append(f"{len(phrases)} risky phrases detected")

    if sentiment > 0.8:
        reasons.append("Overly positive sentiment (possible hype manipulation)")

    if risk_score > 7:
        level = "High Risk"
    elif risk_score > 4:
        level = "Moderate Risk"
    else:
        level = "Low Risk"

    return level, reasons