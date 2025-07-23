import openai

openai.api_base = "http://localhost:11434/v1"
openai.api_key = "AIzaSyA4K46pFwl9KFko_Feh1feyN_yWjGeBTw0"  

def ask_llm(prompt: str) -> str:
    response = openai.ChatCompletion.create(
        model="mistral",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message["content"]
