# AI Document Comparison Assistant

An intelligent Python application that compares two PDF documents using keyword matching and semantic similarity to help users understand how closely related their documents are.

## Project Overview

The AI Document Comparison Assistant is a web application built with Streamlit. It extracts text from PDF files, analyzes keywords, calculates similarity scores, and presents comparison results through visual charts and downloadable PDF reports.

## Features

- **PDF Upload:** Upload two PDF documents for comparison.
- **Text Extraction:** Extract readable text from PDF files.
- **Keyword Similarity:** Compare documents based on their common keywords.
- **Semantic Similarity:** Use Sentence Transformers to measure similarity in meaning.
- **Visual Comparison:** Display similarity scores using a bar chart.
- **Keyword Analysis:** Identify common and unique keywords in each document.
- **PDF Report:** Download a report containing comparison results.
- **Interactive Interface:** Explore results through a simple Streamlit web application.

## Technologies Used

- Python
- Streamlit
- Pandas
- PyPDF
- Sentence Transformers
- Scikit-learn
- ReportLab

## Project Structure

```text
AI-Document-Comparison-Assistant/
│
├── app.py
├── document_reader.py
├── semantic_comparison.py
├── requirements.txt
├── README.md
├── .gitignore
└── screenshots/
    └── document-comparison.png
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/likki-hi/AI-Document-Comparison-Assistant.git
```

### 2. Navigate to the Project Folder

```bash
cd AI-Document-Comparison-Assistant
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Run the Application

```bash
python -m streamlit run app.py
```

The application will open in your browser. Upload two PDF documents to begin comparing them.

## How It Works

1. Upload two PDF documents.
2. Extract text from both documents.
3. Analyze keywords and calculate keyword similarity.
4. Generate text embeddings using a Sentence Transformer model.
5. Calculate semantic similarity using cosine similarity.
6. Display similarity scores, charts, and keyword statistics.
7. Download the comparison report as a PDF.

## Screenshots

Add a screenshot of your running application to the `screenshots` folder.

Once the image is saved as `document-comparison.png`, it will appear here:

![AI Document Comparison Assistant](screenshots/document-comparison.png)

## Learning Outcomes

Through this project, I gained practical experience in:

- Python application development
- PDF text extraction and processing
- Natural language processing concepts
- Text embeddings and cosine similarity
- Data visualization using Streamlit
- Modular Python programming
- Git and GitHub version control

## Future Enhancements

- Support for Word documents and text files
- Advanced similarity analysis
- Highlight matching sections between documents
- Improved report formatting
- Additional document comparison metrics

## Author



**Likitha Kalal**

GitHub: [likki-hi](https://github.com/likki-hi)

## Repository

[AI Document Comparison Assistant](https://github.com/likki-hi/AI-Document-Comparison-Assistant)

---

*This project was developed as a hands-on Python and AI learning project.*

