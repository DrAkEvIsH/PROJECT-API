import os
from huggingface_hub import InferenceClient


def generate_reply(message):
    token = os.getenv("HF_TOKEN")

    if not token:
        return {
            "reply": "HF_TOKEN is not configured.",
            "mode": "error"
        }

    try:
        client = InferenceClient(
            token=token
        )

        response = client.chat.completions.create(
            model="openai/gpt-oss-20b:groq",
            messages=[
                {
                    "role": "system",
                    "content": "You are the AI assistant powering PROJECT API. Give accurate, useful and concise answers."
                },
                {
                    "role": "user",
                    "content": message
                }
            ],
            max_tokens=512
        )

        return {
            "reply": response.choices[0].message.content,
            "mode": "huggingface"
        }

    except Exception as e:
        return {
            "reply": "AI provider error.",
            "mode": "error",
            "error": str(e)
        }
