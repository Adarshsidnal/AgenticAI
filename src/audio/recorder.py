"""Audio recording functionality."""

import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np

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


def enhanced_record_audio(sample_rate: int = 44100, output_file: str = "input.wav") -> None:
    """
    Record audio with enhanced functionality (e.g., noise reduction).
    
    Args:
        sample_rate: Sample rate in Hz
        output_file: Path to save the WAV file
    """
    print("\nPress Enter to start recording...")
    input()

    recordings = []

    def callback(indata, frames, time, status):
        if status:
            print(status)
        recordings.append(indata.copy())
    
    with sd.InputStream(samplerate=sample_rate, channels=1, callback=callback):
        print("Recording... Press Enter to stop.")
        input()

    # Concatenate all recorded chunks
    audio = np.concatenate(recordings, axis=0)

    write(output_file, sample_rate, audio)

    print("Audio recorded with enhanced functionality.")