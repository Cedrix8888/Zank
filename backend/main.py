import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

API_KEY = os.getenv("API_KEY")

async def get_api_key(api_key: str = Header(None)):
    if api_key != API_KEY:
        raise HTTPException(
            status_code=401,
            detail="无效或缺失的API密钥"
        )
    return api_key

class PromptRequest(BaseModel):
    prompt: str

@app.post("/api/ai/generate", dependencies=[Depends(get_api_key)])
async def generate_response(request: PromptRequest):
    ai_response = await process_with_ai(request.prompt)
    return {"response": ai_response}

async def process_with_ai(prompt: str):
    return f"Processed: {prompt}"