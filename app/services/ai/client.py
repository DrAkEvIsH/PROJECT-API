import os
import requests


class AIClient:
    def __init__(self):
        self.api_key = os.environ.get("OPENAI_API_KEY")
        self.api_url = "https://api.openai.com/v1/responses"
        self.model = "gpt-5.6-luna"

    def chat(self, message):
        if not self.api_key:
            raise RuntimeError("OPENAI_API_KEY is not configured.")

        headers = {
            "Authorization": "Bearer " + self.api_key,
            "Content-Type": "application/json",
        }

        data = {
            "model": self.model,
            "input": message,
        }

        response = requests.post(
            self.api_url,
            headers=headers,
            json=data,
            timeout=60,
        )

        if response.status_code != 200:
            try:
                error_data = response.json()
            except Exception:
                error_data = {"raw": response.text}

            raise RuntimeError(
                "OpenAI HTTP {}: {}".format(
                    response.status_code,
                    error_data
                )
            )

        result = response.json()

        # Raw Responses API parsing
        texts = []

        for item in result.get("output", []):
            if item.get("type") != "message":
                continue

            for content in item.get("content", []):
                if content.get("type") == "output_text":
                    texts.append(content.get("text", ""))

        return "".join(texts)