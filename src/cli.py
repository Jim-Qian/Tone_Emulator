import sys
from .ingest import load_user_corpus
from .style_chain import build_style_chain

def main():
    print("=== Personal Style Writer (LangChain CLI) ===")
    print("Loading your writing corpus...")

    try:
        style_corpus = load_user_corpus()
    except Exception as e:
        print(f"Error loading corpus: {e}")
        sys.exit(1)

    chain = build_style_chain(style_corpus)

    print("Ready! Type your instructions (or 'exit' to quit).")
    print("Example: 'Write a reflective paragraph about starting a new job.'")
    print()

    while True:
        user_prompt = input("Prompt> ").strip()
        if user_prompt.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break

        if not user_prompt:
            continue

        length_str = input("How many paragraphs? (default 1) > ").strip()
        try:
            length = int(length_str) if length_str else 1
        except ValueError:
            length = 1

        print("\n--- Generating ---\n")
        try:
            result = chain.invoke({"user_prompt": user_prompt, "length": length})
        except Exception as e:
            print(f"Error during generation: {e}")
            continue

        print(result)
        print("\n------------------\n")

if __name__ == "__main__":
    main()
