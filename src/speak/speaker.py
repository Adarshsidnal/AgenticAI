"""Text-to-speech using pyttsx3."""

import pyttsx3


def speak(text: str) -> None:
    """
    Convert text to speech and play it.
    
    Args:
        text: Text to speak
    """
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
