import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.environ["GROQ_API_KEY"])

PROMPT = "Say hello in Marathi, and write the Marathi word for 'farmer'."

for model in ["openai/gpt-oss-120b", "openai/gpt-oss-20b", "qwen/qwen3.8-27b"]:
    print(f"\n=== {model} ===")
    try:
        resp = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": PROMPT}],
        )
        print(resp.choices[0].message.content)
    except Exception as e:
        print("ERROR:", e)