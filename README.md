**Tone Emulator**
This project will ingest the user's previous writing documents and then can be prompted to write new paragraphs in that user's voice.

------

Tone_Emulator/
  ├─ data/
  │   └─ writings/        # your input docs go here
  ├─ src/
  │   ├─ __init__.py      # 
  │   ├─ ingest.py        # load & preprocess documents
  │   ├─ style_chain.py   # LangChain chain definition
  │   └─ cli.py           # command line interface
  ├─ .env                 # API keys
  ├─ .gitignore
  ├─ requirements.txt
  └─ README.md

------

**How to run locally**
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt

**Start the backend:**
python3 -m src.cli

**Start the frontend (at localhost:8000):**
uvicorn src.server:app --reload