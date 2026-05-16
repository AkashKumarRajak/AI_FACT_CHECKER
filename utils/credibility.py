def calculate_source_trust(urls):

    if not urls:
        return 50

    trusted_domains = [

        "bbc",
        "reuters",
        "wikipedia",
        "gov",
        "edu",
        "openai"

    ]

    score = 50

    for url in urls:

        for domain in trusted_domains:

            if domain in url.lower():
                score += 10

    return min(score, 100)