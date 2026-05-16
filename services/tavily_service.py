import os
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()

client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)


def search_claim(claim):

    response = client.search(
        query=claim,
        search_depth="advanced",
        max_results=5
    )

    results = []

    for item in response.get("results", []):

        results.append({
            "title": item.get("title", "No title"),
            "content": item.get("content", ""),
            "url": item.get("url", "")
        })

    return results