import os
from typing import Type

from jinja2 import Template
from openai import OpenAI
from pydantic import BaseModel

from lib.models.answer_models import Answers

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
TEMPLATE_ENV = os.path.join(PROJECT_ROOT, "prompts")


def load_prompt_template(template_name: str) -> Template:
    """
    Loads a Jinja2 template from the prompts directory.

    Args:
        template_name (str): The name of the template file (without `.jinja2` extension).

    Returns:
        Template: A Jinja2 template object.
    """
    template_path = os.path.join(TEMPLATE_ENV, f"{template_name}.jinja2")
    try:
        with open(template_path, "r") as file:
            return Template(file.read())
    except FileNotFoundError:
        raise FileNotFoundError(
            f"Template file '{template_name}.jinja2' not found in '{TEMPLATE_ENV}'."
        )


# Load the system prompt template
SYSTEM_PROMPT = load_prompt_template("system_prompt").render()


def llm_call(
    user_prompt: str,
    system_prompt: str = SYSTEM_PROMPT,
    response_format: Type[BaseModel] = Answers,
    model: str = "gpt-4o-2024-08-06",
):
    """
    Makes a call to the LLM using the specified user and system prompts.

    Args:
        user_prompt (str): The user prompt to send to the LLM.
        system_prompt (str): The system prompt to set context for the LLM.
        response_format (Type[BaseModel]): The expected format of the LLM response.
        model (str): The model to use for the LLM call.

    Returns:
        Parsed response from the LLM in the specified format.
    """
    # Initialize OpenAI client with the API key from environment variables
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise EnvironmentError("OPENAI_API_KEY environment variable is not set.")

    client = OpenAI(api_key=api_key)

    # Make the API call to OpenAI
    try:
        completion = client.beta.chat.completions.parse(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            response_format=response_format,
        )
        return completion.choices[0].message.parsed
    except Exception as e:
        raise RuntimeError(f"Error during LLM call: {e}")
