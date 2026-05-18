from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import os
import ast

app = FastAPI(title="AI Coding Helper Chatbot")
app.mount("/static", StaticFiles(directory="static"), name="static")

class AnalyzeRequest(BaseModel):
    language: str
    code: str

class AnalyzeResponse(BaseModel):
    summary: str
    issues: list
    corrected_code: str | None = None
    explanation: str | None = None

@app.get("/", response_class=HTMLResponse)
async def root():
    with open("index.html", "r", encoding="utf-8") as f:
        return HTMLResponse(f.read())


@app.post("/analyze", response_model=AnalyzeResponse)
async def analyze(request: AnalyzeRequest):
    """Simple code analyzer with Python syntax checks and placeholders for AI analysis.

    - For Python: performs `ast.parse` to detect SyntaxError and returns explanation.
    - For other languages: returns a guided template response and recommends using an AI model.

    Set `OPENAI_API_KEY` in env to enable full AI-based analysis (not implemented here).
    """
    lang = request.language.lower()
    code = request.code

    # Quick Python syntax check
    if lang in ("python", "py"):
        try:
            ast.parse(code)
        except SyntaxError as e:
            # Return structured explanation: what, why, how to fix
            issue = {
                "type": "SyntaxError",
                "message": str(e),
                "lineno": e.lineno,
                "offset": e.offset,
            }
            corrected = None
            explanation = (
                "A SyntaxError means Python couldn't parse your code. "
                "Check the indicated line and nearby lines for missing colons, parentheses, or indentation."
            )
            return AnalyzeResponse(
                summary="Found Python syntax error",
                issues=[issue],
                corrected_code=corrected,
                explanation=explanation,
            )
        # If no syntax error, provide a friendly placeholder analysis
        summary = "No Python syntax errors detected."
        issues = []
        explanation = (
            "I can also check for common logical problems, suggest optimizations, or produce corrected code. "
            "Send a specific question (e.g., explain this function, find bug, optimize)."
        )
        return AnalyzeResponse(summary=summary, issues=issues, corrected_code=None, explanation=explanation)

    # Generic response for other languages (placeholder)
    summary = f"Received {request.language} code. Basic static checks not implemented for this language."
    issues = []
    explanation = (
        "For non-Python languages, this demo returns a template analysis. "
        "Integrate an LLM (OpenAI/Gemini) to get detailed syntax and logical error detection."
    )
    return AnalyzeResponse(summary=summary, issues=issues, corrected_code=None, explanation=explanation)

@app.get("/health")
async def health():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
