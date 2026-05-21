import sounddevice as sd
from scipy.io.wavfile import write
import whisper
from duckduckgo_search import DDGS
import ollama
import pyttsx3

# -----------------------
# RECORD AUDIO
# -----------------------

duration = 5  # seconds
sample_rate = 44100

print("Speak now...")

audio = sd.rec(
    int(duration * sample_rate),
    samplerate=sample_rate,
    channels=1,
    dtype='int16'
)

sd.wait()

write("input.wav", sample_rate, audio)

print("Audio recorded.")

# -----------------------
# SPEECH TO TEXT
# -----------------------

model = whisper.load_model("base")

result = model.transcribe("input.wav")

query = result["text"]

print(f"\nYou said: {query}")

# -----------------------
# WEB SEARCH
# -----------------------

search_results = []

with DDGS() as ddgs:
    results = ddgs.text(query, max_results=3)

    for r in results:
        search_results.append(r["body"])

search_text = "\n".join(search_results)

# -----------------------
# ASK LLM
# -----------------------

prompt = f"""
Answer the user's question using the web results below.

Question:
{query}

Web Results:
{search_text}
"""

response = ollama.chat(
    model="qwen3:4b",
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

# -----------------------
# TEXT TO SPEECH
# -----------------------

engine = pyttsx3.init()

engine.say(answer)

engine.runAndWait()