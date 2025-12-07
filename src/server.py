from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from .ingest import load_user_corpus
from .style_chain import build_style_chain

# ---------- Setup ----------

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for dev; you can restrict later
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
    style: str = "concise"  # "concise" | "elaborate"


class GenerateResponse(BaseModel):
    text: str


# ---------- Routes ----------

@app.post("/generate", response_model=GenerateResponse)
async def generate(req: GenerateRequest):
    # Adjust the prompt based on style
    if req.style == "elaborate":
        styled_prompt = (
            req.prompt
            + "\n\nWrite with more detail, nuance, and elaboration. Use richer explanations and slightly longer sentences."
        )
    else:
        # default: concise
        styled_prompt = (
            req.prompt
            + "\n\nWrite in a concise, to-the-point style with minimal fluff."
        )

    result = chain.invoke(
        {
            "user_prompt": styled_prompt,
            "length": req.length,
        }
    )

    return GenerateResponse(text=result)
