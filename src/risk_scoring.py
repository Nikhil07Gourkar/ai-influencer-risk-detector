def calculate_risk_score(risk_phrases, sentiment_score, has_disclaimer):

    risk_score = 0

    # Phrase risk
    risk_score += len(risk_phrases) * 2

    # Extreme positive sentiment
    if sentiment_score > 0.7:
        risk_score += 2

    # No disclaimer penalty
    if not has_disclaimer:
        risk_score += 2

    # Normalize
    if risk_score > 10:
        risk_score = 10

    return risk_score