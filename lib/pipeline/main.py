import os
import sys

from rich import print as pretty

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from lib.app.rental_check import deploy_streamlit
from lib.pipeline.llm import llm_call, load_prompt_template
from lib.pipeline.process import PDFProcessor


def process_contract(file_path: str) -> dict:
    """
    Processes a contract by extracting text from a PDF file,
    limiting the text to 30,000 characters, and generating an LLM response.

    Args:
        file_path (str): The full path of the PDF file to process.

    Returns:
        dict: The response from the LLM call, containing insights or structured output from the contract.

    Raises:
        FileNotFoundError: If the PDF file is not found.
        RuntimeError: If an error occurs during LLM processing.
    """
    # Create a PDFProcessor instance
    processor = PDFProcessor(file_path)

    # Extract text from the PDF
    processor.extract_text()

    # Read the processed text
    processed_text = processor.read_processed_text()

    # Limit to 30,000 characters (to comply with TPM limit)
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


if __name__ == "__main__":
    import streamlit as st

    st.title("Rental Contract Processor")

    # File upload widget
    uploaded_file = st.file_uploader("Upload a rental contract PDF:", type=["pdf"])

    if uploaded_file is not None:
        # Save the uploaded file to the raw data directory
        raw_data_dir = os.path.join(os.path.dirname(__file__), "../../data/raw")
        os.makedirs(raw_data_dir, exist_ok=True)

        file_path = os.path.join(raw_data_dir, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.read())
        st.success(f"File {uploaded_file.name} uploaded successfully!")

        if st.button("Process Contract"):
            try:
                pretty("[bold green]Processing contract...[/bold green]")
                pipeline_output = process_contract(file_path=file_path)
                pretty("[bold green]Processing completed successfully![/bold green]")
                deploy_streamlit(pipeline_output)
            except Exception as e:
                st.error(f"Error: {e}")
