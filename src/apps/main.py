# src/main.py
"""Main module for the project."""
# from openai import OpenAI
from langchain_openai.llms import OpenAI
from configs.env_configs import OPENAI_API_KEY


def print_msg(greeting: str) -> None:
    """_summary_

    Args:
        greeting (str): _description_
    """
    print(greeting)


def main() -> None:
    """_summary_
    """
    print_msg("Hello, World!")
    print_msg("Hola, Mundo!")
    print_msg("Goodbye, World!")


if __name__ == "__main__":
    main()
    llm = OpenAI(api_key=OPENAI_API_KEY)

    result = llm.invoke("Write a very short poen about a cat.")
    print(result)
