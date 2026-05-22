import json

from src.llm.ollama_Client import ask_llm

def extract_intent(question):
    prompt = f"""
    You are a Junos configuration assistant.

    Convert the user question into JSON.

    Examples:

    Question:
    Is MPLS configured on et-0/0/1?

    Output:
    {{
    "intent": "interface_feature_check",
    "interface": "et-0/0/1",
    "feature": "mpls"
    }}

    Question:
    Does customer use BGP?

    Output:
    {{
    "intent": "feature_check",
    "feature": "bgp"
    }}

    Now answer this:

    Question:
    {question}
    """

    response = ask_llm(prompt)
    try:
        intent_data = json.loads(response)
        return intent_data
    except json.JSONDecodeError:
        print("Failed to parse JSON response from LLM.")
        return None