# RentalCheck: Automated Information Extraction from Tenancy Agreements

RentalCheck is a tool designed to automate the extraction of key information from tenancy agreements using GPT. This project streamlines the process of analyzing tenancy agreements, enabling users to quickly extract and interpret essential details such as tenant names, property details, rent amounts, and contract terms. Citations are provided for all answers and become visible when clicking on individual answers.

---

## Table of Contents

1. [Features](#features)
2. [Getting Started](#getting-started)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Limitations](#limitations)
6. [Future Work](#future-work)

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

Run the main script and upload a tenancy agreement (PDF) when prompted:

   ```zsh
   streamlit run lib/pipeline/main.py
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

---
