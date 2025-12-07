**Tone Emulator**
This project will ingest the user's previous writing documents and then can be prompted to write new paragraphs in that user's voice.

------
**Code Structure:**

```
Tone_Emulator/
  ├─ data/
  │   └─ writings/        # Your input files
  ├─ env/
  ├─ frontend/
  │   └─ index.html/      
  ├─ src/
  │   ├─ __init__.py      
  |   ├─ cli.py           # Command line interface
  │   ├─ ingest.py        # Load & preprocess documents locally (without contacting LLM APIs)
  │   ├─ server.py        # Backend website APIs
  │   └─ style_chain.py   # LangChain chain definition (contacts LLM APIs)
  ├─ .env                 # API keys
  ├─ .gitignore
  ├─ README.md
  └─ requirements.txt
```

------
**How to Run Locally:**
This project has 2 independent frontends: command line or web browser.

**For Both:**
1. python3 -m venv env
2. source env/bin/activate
3. pip3 install -r requirements.txt

**Command Line:**
1. python3 -m src.cli

**Web Browser:**
1. uvicorn src.server:app --reload
2. Open the index.html