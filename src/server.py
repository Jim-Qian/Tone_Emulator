from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from .ingest import load_user_corpus
from .style_chain import build_style_chain

# ---------- Setup ----------

app = FastAPI()

# Allow frontend to call API (localhost dev)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # you can tighten this later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

print("Loading style corpus...")
style_corpus = load_user_corpus()
chain = build_style_chain(style_corpus)
print("Style chain ready.")


# ---------- Models ----------

class GenerateRequest(BaseModel):
    prompt: str
    length: int = 1
    meme_mode: bool = False
    emoji_mode: bool = False


class GenerateResponse(BaseModel):
    text: str

# ---------- Routes ----------

@app.post("/generate", response_model=GenerateResponse)
async def generate(req: GenerateRequest):
    # Call your LangChain chain
    result = chain.invoke({"user_prompt": req.prompt, "length": req.length})

    return GenerateResponse(text=result)
