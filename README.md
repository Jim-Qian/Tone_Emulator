**Tone Emulator**
This project will ingest the user's previous writing documents and then can be prompted to write new paragraphs in that user's voice.

my-style-writer/
  ├─ data/
  │   └─ writings/        # your input docs go here
  ├─ src/
  │   ├─ ingest.py        # load & preprocess documents
  │   ├─ style_chain.py   # LangChain chain definition
  │   └─ cli.py           # command line interface
  ├─ .env                 # API keys
  ├─ requirements.txt
  └─ README.md

python3 -m venv env
source env/bin/activate         
pip3 install -r requirements.txt