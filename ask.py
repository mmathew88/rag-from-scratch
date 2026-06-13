import sys
import ollama

DIVIDER = "─" * 50

def ask_llm(question: str, model: str = "llama3.2") -> dict:
    """
    Send a question to a local Ollama model.
    Returns dict with answer and model name.
    """
    response = ollama.chat(
        model=model,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a concise technical teacher. "
                    "Answer clearly and briefly. "
                    "If relevant, give a one-line concrete example. "
                    "Do not add preamble or filler phrases."
                )
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    return {
        "answer": response["message"]["content"],
        "model": model,
    }

def print_result(question: str, result: dict):
    print(DIVIDER)
    print(f"Question: {question}")
    print(DIVIDER)
    print(result["answer"])
    print(DIVIDER)
    print(f"Model: {result['model']}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python ask.py \"your question here\"")
        print("Example: python ask.py \"What is a vector database?\"")
        sys.exit(1)

    question = " ".join(sys.argv[1:])

    if not question.strip():
        print("Error: question cannot be empty")
        sys.exit(1)

    result = ask_llm(question)
    print_result(question, result)

if __name__ == "__main__":
    main()