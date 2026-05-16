def calculate_confidence(claim, sources, verdict):

    score = 40

    claim = claim.lower()

    # SOURCE COUNT BOOST
    source_count = len(sources)

    if source_count >= 5:
        score += 20

    elif source_count >= 3:
        score += 15

    elif source_count >= 1:
        score += 10

    # TRUSTED DOMAINS
    trusted_domains = [
        ".gov",
        ".edu",
        "reuters.com",
        "bbc.com",
        "wikipedia.org",
        "openai.com",
        "google.com",
        "ibm.com",
        "whitehouse.gov"
    ]

    trust_score = 0

    for source in sources:

        if isinstance(source, str):
            url = source.lower()

        elif isinstance(source, dict):
            url = source.get("url", "").lower()

        else:
            continue

        for domain in trusted_domains:
            if domain in url:
                trust_score += 8
                break

    score += trust_score

    # VERDICT BOOST
    if "true" in verdict.lower():
        score += 15

    # FACTUAL CLAIM BOOST
    factual_keywords = [
        "is",
        "was",
        "president",
        "capital",
        "invented",
        "founded",
        "located"
    ]

    for word in factual_keywords:
        if word in claim:
            score += 5
            break

    return min(score, 98)