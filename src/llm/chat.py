"""LLM interaction using Ollama."""

import ollama


def query_llm(query: str, search_results: str, model: str = "qwen3:4b") -> str:
    """
    Query LLM with question and web search results.
    
    Args:
        query: User's question
        search_results: Web search results to provide context
        model: LLM model to use
    
    Returns:
        LLM response
    """
    prompt = f"""
Answer the user's question using the web results below.

Question:
{query}

Web Results:
{search_results}
"""
    
    response = ollama.chat(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    
    answer = response["message"]["content"]
    print("\nAssistant:")
    print(answer)
    return answer
