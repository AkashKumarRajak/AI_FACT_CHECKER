def detect_category(claim):

    claim = claim.lower()

    categories = {

        "Politics": [
            "president",
            "election",
            "government",
            "minister",
            "trump",
            "biden",
            "modi",
            "parliament",
            "politics"
        ],

        "Sports": [
            "football",
            "cricket",
            "virat",
            "ronaldo",
            "messi",
            "sports",
            "fifa",
            "ipl",
            "msd",
            "dhoni",
            "mahendra singh dhoni",
            "cool captain",
            "captain"
        ],

        "Technology": [
            "ai",
            "artificial intelligence",
            "python",
            "computer",
            "software",
            "openai",
            "chatgpt",
            "technology"
        ],

        "Health": [
            "covid",
            "vaccine",
            "medicine",
            "health",
            "doctor",
            "disease"
        ],

        "Finance": [
            "bitcoin",
            "crypto",
            "stock",
            "market",
            "money",
            "finance"
        ]
    }

    scores = {}

    for category, keywords in categories.items():

        score = 0

        for keyword in keywords:

            if keyword in claim:
                score += 1

        scores[category] = score

    best_category = max(
        scores,
        key=scores.get
    )

    if scores[best_category] == 0:
        return "General"

    return best_category

