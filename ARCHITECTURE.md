# Project Architecture

## Project Structure

```
├── main.py                    # Entry point - orchestrates the workflow
├── src/
│   ├── __init__.py           # Package initialization
│   ├── audio/
│   │   ├── __init__.py
│   │   └── recorder.py       # Audio recording from microphone
│   ├── nlp/
│   │   ├── __init__.py
│   │   └── transcriber.py    # Speech-to-text using Whisper
│   ├── search/
│   │   ├── __init__.py
│   │   └── web_search.py     # Web search using DuckDuckGo
│   ├── llm/
│   │   ├── __init__.py
│   │   └── chat.py           # LLM queries using Ollama
│   └── speak/
│       ├── __init__.py
│       └── speaker.py        # Text-to-speech using pyttsx3
```

## Module Descriptions

### `src.audio`

Handles audio recording from the user's microphone and saves it to a WAV file.

- **recorder.py**: `record_audio()` - Records audio with configurable duration and sample rate

### `src.nlp`

Handles natural language processing and speech-to-text conversion.

- **transcriber.py**: `transcribe_audio()` - Transcribes audio using Whisper model

### `src.search`

Handles web search functionality to provide context for the LLM.

- **web_search.py**: `search_web()` - Searches the web using DuckDuckGo API

### `src.llm`

Handles interaction with the local LLM (Ollama).

- **chat.py**: `query_llm()` - Sends queries to LLM with web search context

### `src.speak`

Handles text-to-speech conversion to speak responses back to the user.

- **speaker.py**: `speak()` - Converts text to speech using pyttsx3

## Workflow

```
User speaks → Record Audio → Transcribe to Text → Web Search
    ↓
    Query LLM with search results → Convert to Speech → Play to User
```

## Running the Application

```bash
python main.py
```

## Benefits of Modular Architecture

1. **Separation of Concerns**: Each module has a single responsibility
2. **Reusability**: Modules can be used independently in other projects
3. **Testability**: Each module can be tested in isolation
4. **Maintainability**: Easier to locate and fix bugs
5. **Scalability**: Easy to add new features or swap implementations
