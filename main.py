"""
Main entry point for Agentic AI application.

This application provides a voice-based AI assistant that:
1. Records audio from the user
2. Transcribes it to text using Whisper
3. Searches the web for relevant information
4. Queries an LLM for intelligent responses
5. Speaks the response back to the user
"""

from src.audio import record_audio
from src.nlp import transcribe_audio
from src.search import search_web
from src.llm import query_llm
from src.speak import speak


def main() -> None:
    """Run the main agentic AI workflow."""
    # Record audio from user
    record_audio(duration=5, sample_rate=44100, output_file="input.wav")
    
    # Transcribe audio to text
    query = transcribe_audio(audio_file="input.wav", model_size="base")
    
    # Search the web for context
    search_results = search_web(query, max_results=3)
    
    # Query LLM with question and search results
    answer = query_llm(query, search_results, model="qwen3:4b")
    
    # Speak the answer
    speak(answer)


if __name__ == "__main__":
    main()