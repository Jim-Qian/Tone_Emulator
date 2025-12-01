import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

def build_style_chain(style_corpus: str):
    """
    Build a LangChain pipeline that mimics the user's voice.
    """

    llm = ChatOpenAI(
        model="gpt-4o-mini",  # or another chat model you have access to
        temperature=0.9,
    )

    system_prompt = """
You are a writing assistant that strictly imitates the user's writing style.

You are given a corpus of the user's writing. Study their tone, sentence length,
word choice, and overall voice.

When asked to write something new:
- Maintain the same voice, cadence, and personality as the corpus.
- Do NOT copy sentences directly; write fresh content.
- Match approximate length and level of detail requested.
- Avoid saying things like "As an AI" or "Based on your style".
- Just write the paragraph(s) directly in that style.

User's writing corpus:
---
{style_corpus}
---
""".strip()

    human_prompt = """
Write new text in the user's voice.

Topic / instructions:
{user_prompt}

Length: about {length} paragraph(s).
""".strip()

    # Build prompt with variables style_corpus, user_prompt, length
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", human_prompt),
        ]
    )

    # ✅ Bake in the style_corpus here
    prompt = prompt.partial(style_corpus=style_corpus)

    # Then build the chain
    chain = prompt | llm | StrOutputParser()

    return chain
