#📝A2Z Extractive Summarizer

A2Z Summarizer is a Python-based web application that generates extractive summaries from text, PDFs, Word documents, and web articles. The app supports multiple summarization algorithms and provides a modern, interactive interface using Streamlit.

Features

Summarize plain text, PDFs, Word documents, and web articles.

Choose from four extractive algorithms:

LSA (Latent Semantic Analysis)

LexRank

Luhn

TextRank

Interactive Streamlit interface with sidebar controls.

Modern cards and buttons for a professional look.

Download summary as a .txt file.

Robust handling for URL errors / paywalled articles.

Tech Stack

Python 3.10+

NLTK – Text tokenization & preprocessing

Sumy – Extractive summarization algorithms

newspaper3k – Web article scraping

PyPDF2 – PDF parsing

python-docx – Word document parsing

Streamlit – Interactive frontend

HTML & CSS – Custom styling

Installation

Clone the repository:

git clone <your-repo-url>
cd A2Z-Summarizer


Install dependencies:

pip install -r requirements.txt


Example requirements.txt:

streamlit
nltk
sumy
PyPDF2
python-docx
newspaper3k
beautifulsoup4
lxml


Download NLTK punkt models:

import nltk
nltk.download("punkt")
nltk.download("punkt_tab")

Usage

Run the app:

streamlit run app.py


Use the sidebar to:

Select input type: Text, PDF, Word, or Web URL

Select summarization algorithm

Choose number of sentences

Paste/upload your text or enter a URL.

Click “Generate Summary”.

View the summary in the card and download it as .txt.

Screenshots


Main interface with text input and sidebar.


PDF/Word upload and summary card.

Notes

Some websites (e.g., ScienceDirect, IEEE) may block scraping, so use PDF uploads for paywalled content.

Works best for English text.

Lightweight and simple extractive summarizer for quick results.

License

This project is open-source and free to use under the MIT License
.

✅ This README is professional, clear, and complete for GitHub or portfolio submission.
