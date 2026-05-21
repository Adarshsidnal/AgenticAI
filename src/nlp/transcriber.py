"""Speech-to-text transcription using Whisper."""

import whisper


def transcribe_audio(audio_file: str = "input.wav", model_size: str = "base") -> str:
    """
    Transcribe audio file to text using Whisper.
    
    Args:
        audio_file: Path to audio file
        model_size: Whisper model size (tiny, base, small, medium, large)
    
    Returns:
        Transcribed text
    """
    model = whisper.load_model(model_size)
    result = model.transcribe(audio_file)
    query = result["text"]
    print(f"\nYou said: {query}")
    return query
