import streamlit as st
import nltk
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.summarizers.text_rank import TextRankSummarizer
import PyPDF2
import docx
from newspaper import Article, ArticleException

# Download NLTK punkt
nltk.download("punkt")
nltk.download("punkt_tab")

# =======================
# Helper Functions
# =======================
def read_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() or ""
    return text

def read_docx(file):
    doc = docx.Document(file)
    return " ".join([para.text for para in doc.paragraphs])

def read_url(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        text = article.text
        if not text.strip():
            st.warning("⚠️ No text could be extracted from this URL. Try uploading a PDF instead.")
            return ""
        return text
    except ArticleException as e:
        st.warning(f"⚠️ Unable to download article: {e}. Try PDF upload instead.")
        return ""
    except Exception as e:
        st.warning(f"⚠️ Error reading URL: {e}")
        return ""

def summarize_extractive(text, algo="LSA", num_sentences=3):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))

    if algo == "LSA":
        summarizer = LsaSummarizer()
    elif algo == "LexRank":
        summarizer = LexRankSummarizer()
    elif algo == "Luhn":
        summarizer = LuhnSummarizer()
    elif algo == "TextRank":
        summarizer = TextRankSummarizer()
    else:
        summarizer = LsaSummarizer()

    summary = summarizer(parser.document, num_sentences)
    return " ".join([str(sentence) for sentence in summary])

# =======================
# Streamlit UI
# =======================
st.set_page_config(page_title="A2Z Summarizer", page_icon="📝", layout="wide")

# Custom CSS for professional look
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .title {
        text-align: center;
        font-size: 36px;
        font-weight: bold;
        color: #2c3e50;
        margin-bottom: 10px;
    }
    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #7f8c8d;
        margin-bottom: 30px;
    }
    .card {
        background-color: blue; 
        padding: 10px 15px;       
        border-radius: 8px;        
        box-shadow: 0px 2px 5px rgba(0,0,0,0.05);
        margin-top: 15px;
    }
    .summary-text {
        font-size: 15px;
        line-height: 1.5;
        color: white;
    }
    button[data-baseweb="button"] {
        padding: 5px 15px !important;
        font-size: 14px !important;
        background-color: #3498db !important;
        color: white !important;
        border-radius: 8px !important;
    }
    button[data-baseweb="button"]:hover {
        background-color: #2980b9 !important;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="title">📝 A2Z Extractive Summarizer</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Summarize Text, PDFs, Word Docs, and Web Articles in Seconds</div>', unsafe_allow_html=True)

# Sidebar
st.sidebar.header("⚙️ SUMMARIZATIONS")
option = st.sidebar.radio("Choose Input Type:", ["✍️ Text", "📄 PDF", "📝 Word", "🌐 Web URL"])
algo = st.sidebar.selectbox("Choose Algorithm:", ["LSA", "LexRank", "Luhn", "TextRank"])
num_sentences = st.sidebar.slider("Number of sentences:", 1, 10, 3)

# Input Section
input_text = ""
if option == "✍️ Text":
    input_text = st.text_area("Paste your text here:", height=200)

elif option == "📄 PDF":
    uploaded_file = st.file_uploader("Upload PDF", type="pdf")
    if uploaded_file:
        input_text = read_pdf(uploaded_file)

elif option == "📝 Word":
    uploaded_file = st.file_uploader("Upload Word Document", type="docx")
    if uploaded_file:
        input_text = read_docx(uploaded_file)

elif option == "🌐 Web URL":
    url = st.text_input("Enter a web article URL:")
    if url:
        input_text = read_url(url)

# Summarization
if input_text and st.button("🚀 Generate Summary"):
    with st.spinner("Processing..."):
        try:
            summary = summarize_extractive(input_text, algo, num_sentences)
            st.markdown('<div class="card"><h3>✅ Summary:</h3>', unsafe_allow_html=True)
            st.markdown(f'<div class="summary-text">{summary}</div></div>', unsafe_allow_html=True)

            st.download_button(
                label="📥 Download Summary",
                data=summary,
                file_name="summary.txt",
                mime="text/plain"
            )
        except Exception as e:
            st.error(f"⚠️ Error: {e}")
