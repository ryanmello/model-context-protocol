import os

import anthropic
from dotenv import load_dotenv

load_dotenv()

print("hello world")

client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY")
)

PROMPT = (
    "find 201122 removed from 316043 and then find the square root of the result. "
    "Return this value **only** with no other words."
)

response = client.messages.create(
    model="claude-3-7-sonnet-20250219",
    max_tokens=1024,
    messages=[{"role": "user", "content": PROMPT}],
)

print(response.content)
