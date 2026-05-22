"""
Main entry point for Agentic AI application.

This application provides a voice-based AI assistant that:
1. Records audio from the user
2. Transcribes it to text using Whisper
3. Searches the config for relevant information
4. Queries an LLM for intelligent responses
5. Speaks the response back to the user
"""

from src.audio import record_audio , enhanced_record_audio
from src.nlp import transcribe_audio
from src.search import search_web
from src.llm import query_llm
from src.speak import speak
from src.analyzer.parser import load_config
from src.analyzer.queries import (has_keyword, interface_has_keyword)
from src.analyzer.agent import extract_intent
import json

def main() -> None:

    """Run the main agentic AI workflow."""
    # Record audio from user
    enhanced_record_audio(sample_rate=44100, output_file="input.wav")
    
    # Transcribe audio to text
    query = transcribe_audio(audio_file="input.wav", model_size="base")

    config = load_config()

    intent_raw = extract_intent(query)

    if intent_raw is None:
        print("Could not extract intent from the query.")
        return
    
    print(f"Extracted intent: {json.dumps(intent_raw, indent=2)}")
    intent = json.loads(json.dumps(intent_raw))


    if intent["intent"] == "feature_check":

        feature = intent["feature"]

        result = has_keyword(config, feature)

        print(f"\nAnswer: {result}")

    elif intent["intent"] == "interface_feature_check":

        interface = intent["interface"]
        feature = intent["feature"]

        result = interface_has_keyword(
            config,
            interface,
            feature
        )
    
    # Search the web for context
    #search_results = search_web(query, max_results=3)
    
    # Query LLM with question and search results
    #answer = query_llm(query, search_results, model="qwen3:4b")
    
    # Speak the answer
    answer = f"The answer to your question is: {result}"
    speak(answer)


if __name__ == "__main__":
    main()