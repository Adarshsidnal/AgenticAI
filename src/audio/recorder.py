"""Audio recording functionality."""

import sounddevice as sd
from scipy.io.wavfile import write


def record_audio(duration: int = 5, sample_rate: int = 44100, output_file: str = "input.wav") -> None:
    """
    Record audio from microphone and save to file.
    
    Args:
        duration: Recording duration in seconds
        sample_rate: Sample rate in Hz
        output_file: Path to save the WAV file
    """
    print("Speak now...")
    
    audio = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype='int16'
    )
    
    sd.wait()
    
    write(output_file, sample_rate, audio)
    
    print("Audio recorded.")
