# RentalCheck: Automated Information Extraction from Rental Contracts

RentalCheck is a tool designed to automate the extraction of key information from rental contracts using advanced AI language models. This project streamlines the process of analyzing rental agreements, enabling users to quickly extract and interpret essential details such as tenant names, property details, rent amounts, and contract terms.

---

## Table of Contents

1. [Features](#features)
2. [Getting Started](#getting-started)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Project Structure](#project-structure)
6. [Examples](#examples)
7. [Limitations](#limitations)
8. [Future Work](#future-work)
9. [License](#license)

---

## Features

- **PDF Parsing**: Extracts text from rental contracts in PDF format.
- **AI-Powered Insights**: Uses large language models (LLMs) to analyze and interpret the extracted text.
- **Customizable Templates**: Supports Jinja2 templates for generating prompts for AI models.
- **Token-Limited Processing**: Ensures compatibility with LLM token limits by truncating text as needed.
- **Extensibility**: Modular pipeline design for adding additional processing or custom logic.

---

## Getting Started

### Prerequisites

To use RentalCheck, you need the following:

- Python 3.8 or higher
- An OpenAI API key for accessing LLMs (e.g., GPT models)
- pip for installing dependencies

---

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/RentalCheck.git
   cd RentalCheck
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up your OpenAI API key:

   ```bash
   export OPENAI_API_KEY="your_openai_api_key"  # On Windows: set OPENAI_API_KEY="your_openai_api_key"
   ```

---

## Usage

### Extracting Information from a Rental Contract

1. Place the rental contract PDF file in the `data/raw/` directory.
2. Run the main script with the filename of the raw PDF:

   ```bash
   python main.py "Contract_Name.pdf"
   ```

3. The extracted text will be saved to `data/processed/Contract_Name.txt`, and key information will be displayed in the terminal.

### Example Output

```json
{
    "tenant_name": "John Doe",
    "property_address": "123 Main Street, Springfield, USA",
    "monthly_rent": "$1200",
    "lease_start_date": "2024-01-01",
    "lease_end_date": "2025-01-01"
}
```

---

## Project Structure

```
RentalCheck/
├── data/
│   ├── raw/                # Raw PDF contracts
│   ├── processed/          # Processed text files
├── lib/
│   ├── pipeline/
│   │   ├── process.py      # PDF processing logic
│   │   ├── llm.py          # LLM interaction and prompt generation
│   ├── models/
│   │   ├── answer_models.py # Pydantic models for structured responses
├── wip/
│   ├── tests.ipynb         # Testing and experimentation
├── prompts/                # Jinja2 templates for LLM prompts
├── README.md               # Project documentation
├── main.py                 # Main script
```

---

## Examples

### Extract Text from a Rental Contract

```python
from lib.pipeline.process import PDFProcessor

processor = PDFProcessor("Contract_Name.pdf")
processor.extract_text()
text = processor.read_processed_text()
print(text)
```

### Analyze Extracted Text with LLM

```python
from lib.pipeline.llm import load_prompt_template, llm_call

prompt = load_prompt_template("user_prompt").render(contract="Extracted contract text")
response = llm_call(user_prompt=prompt)
print(response)
```

---

## Limitations

- Token limit: Currently supports up to 30,000 characters per document due to LLM token constraints.
- Limited context: Information extraction relies on well-structured contracts; complex layouts may require additional processing.

---

## Future Work

- Integrate models with longer context windows.
- Add support for multi-file processing.
- Expand extraction capabilities for more contract types.
- Implement a web-based interface for easier usage.

---
