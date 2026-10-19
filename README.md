
# AI Document Comparison Assistant

A Python-based web application that compares two PDF documents using keyword analysis and semantic similarity.

## Features

- Upload two PDF documents
- Extract and display PDF text
- Calculate keyword similarity
- Calculate semantic similarity using sentence-transformer embeddings
- Display a similarity comparison chart
- Identify common and unique keywords
- Download a PDF comparison report

## Technologies Used

- Python
- Streamlit
- Pandas
- pypdf
- Sentence Transformers
- Scikit-learn
- ReportLab

## Installation

Clone the repository:

```bash
git clone https://github.com/likki-hi/AI-Document-Comparison-Assistant.git
```

Open the project folder and install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run the Application

```bash
python -m streamlit run app.py
```

Open the local URL displayed in the terminal, usually http://localhost:8501.

## Project Structure

```text
AI-Document-Comparison-Assistant/
├── app.py
├── document_reader.py
├── semantic_comparison.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Author

Likitha Kalal
