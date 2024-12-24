from rich import print as pretty

from lib.pipeline.llm import llm_call, load_prompt_template
from lib.pipeline.process import PDFProcessor


def process_contract(file_name: str) -> dict:
    """
    Processes a contract by extracting text from a PDF file,
    limiting the text to 30,000 characters, and generating an LLM response.

    Args:
        file_name (str): The name of the PDF file to process (must be located in the raw data directory).

    Returns:
        dict: The response from the LLM call, containing insights or structured output from the contract.

    Raises:
        FileNotFoundError: If the PDF file is not found.
        RuntimeError: If an error occurs during LLM processing.
    """
    # Create a PDFProcessor instance
    processor = PDFProcessor(file_name)

    # Extract text from the PDF
    processor.extract_text()

    # Read the processed text
    processed_text = processor.read_processed_text()

    # Limit to 30,000 characters (to comply with TPM limit)
    # TODO: Use another API version/model with a longer context window
    document = processed_text[:30000]

    # Render the user prompt
    user_prompt = load_prompt_template(template_name="user_prompt").render(
        contract=document
    )

    # Call the LLM and pretty-print the response
    try:
        response = llm_call(user_prompt=user_prompt)
        pretty(response)
        return response
    except Exception as e:
        raise RuntimeError(f"Error during LLM processing: {e}")
