from openai import OpenAI
from dotenv import load_dotenv
import os

# Load .env variables
load_dotenv()

# OpenRouter Client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

def verify_claim(claim, evidence):

    prompt = f"""
    You are an AI Fact Verification Assistant.

    Analyze the following claim using the provided evidence.

    Claim:
    {claim}

    Evidence:
    {evidence}

    Return response in this format:

    Verdict:
    (True / False / Misleading / Unverified)

    Explanation:
    (Explain reasoning clearly)

    Contradictions:
    (Mention conflicting evidence if any)

    Final Summary:
    (Provide final conclusion)
    """

    response = client.chat.completions.create(
        model="openai/gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content