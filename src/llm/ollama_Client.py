import ollama

def ask_llm(prompt):
    response =ollama.chat(
        model='qwen3:4b',
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )
    return response["message"]["content"]

