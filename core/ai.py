import requests

OLLAMA_URL = "http://localhost:11434/api/generate"


def ask_ai(prompt):
    payload = {
        "model": "llama3.2:3b",
        "prompt": prompt,
        "stream": False,
    }

    response = requests.post(OLLAMA_URL, json=payload)
    return response.json()["response"]
