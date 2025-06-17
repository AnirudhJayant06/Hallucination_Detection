from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

class TranslationRequest(BaseModel):
    input: str

def mock_translate_to_hinglish(text):
    return f"{text} (translated to Hinglish 🔄)"

@app.post("/translate")
async def translate(request: TranslationRequest):
    translated = mock_translate_to_hinglish(request.input)
    return {"translation": translated}