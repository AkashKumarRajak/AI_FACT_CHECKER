def calculate_risk_score(claim):

    claim = claim.lower()

    fake_words = [
        "shocking",
        "secret",
        "viral",
        "exposed",
        "breaking",
        "government hiding",
        "100% cure",
        "miracle",
        "click here",
        "must watch"
    ]

    score = 0

    for word in fake_words:
        if word in claim:
            score += 20

    if score >= 60:
        return "HIGH"

    elif score >= 30:
        return "MEDIUM"

    else:
        return "LOW"