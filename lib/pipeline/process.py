from pathlib import Path

import pymupdf


class PDFProcessor:
    """
    A class to process PDF files and extract text.
    """

    def __init__(self, file_name: str):
        """
        Initializes the PDFProcessor with the input and output file paths.

        Parameters:
        file_name (str): The name of the input PDF file (without the directory).
        """
        # Dynamically determine the project root and directories
        self.project_root = Path(__file__).resolve().parents[2]
        self.raw_dir = self.project_root / "data" / "raw"
        self.processed_dir = self.project_root / "data" / "processed"

        # Set input and output paths
        self.input_path = self.raw_dir / file_name
        self.output_path = self.processed_dir / f"{Path(file_name).stem}.txt"

    def extract_text(self):
        """
        Extracts text from the PDF and writes it to the output file.
        """
        try:
            # Open the PDF document
            doc = pymupdf.open(self.input_path)

            # Open the output file
            with open(self.output_path, "wb") as out:
                for page in doc:  # Iterate through document pages
                    text = page.get_text().encode("utf8")  # Get plain text (UTF-8)
                    out.write(text)  # Write text of page
                    out.write(bytes((12,)))  # Write page delimiter (form feed 0x0C)
            print("Text extracted and saved.")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            # Close the document
            doc.close()

    def read_processed_text(self):
        """
        Reads and returns the content of the processed text file.

        Returns:
        str: The content of the processed text file.
        """
        try:
            with open(self.output_path, "r", encoding="utf8") as file:
                return file.read()
        except FileNotFoundError:
            print(f"Processed file not found: {self.output_path}")
            return None
