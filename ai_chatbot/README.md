# AI Coding Helper Chatbot (Demo)

This repository contains a minimal demo of an AI Coding Helper Chatbot. It's intended as a starting point for a coding tutor that can explain concepts, detect/fix code errors, and provide examples.

Features (demo):
- Python syntax checks via `ast`.
- Simple FastAPI backend and a minimal frontend.
- Placeholders for integrating an LLM (OpenAI/Gemini) to extend capabilities.

Quick start

1. Create a Python virtual environment and install dependencies:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

2. Run the app:

```bash
python app.py
```

3. Open http://localhost:8000 in your browser.

Notes
- To enable AI-powered analysis, add your OpenAI/Gemini integration in `app.py` and set `OPENAI_API_KEY` as an environment variable.
- This demo intentionally keeps analysis simple and explainable for learning purposes.

Next steps
- Add LLM integration to produce corrected code and detailed explanations.
- Add server-side compilation/linting tools for Java/JS/C/C++.
- Persist user sessions and history with a DB (e.g., MongoDB).