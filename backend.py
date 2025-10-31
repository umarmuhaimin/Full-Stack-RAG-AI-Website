# ==============================
# 🎯 SECTION 1: IMPORTS
# ==============================

from flask import Flask, request, Response, stream_with_context, jsonify
from flask_cors import CORS
import os
import json
import time
from werkzeug.utils import secure_filename
from pathlib import Path
from datetime import datetime, timedelta

# ==============================
# 🎯 SECTION 2: PDF HANDLING
# ==============================

try:
    from pypdf import PdfReader
    PDF_SUPPORT = True
    print("✅ PDF support enabled (using pypdf)")
except ImportError:
    try:
        from PyPDF2 import PdfReader
        PDF_SUPPORT = True
        print("✅ PDF support enabled (using PyPDF2)")
    except ImportError:
        PDF_SUPPORT = False
        print("⚠️ PDF support disabled (install: pip install pypdf)")

# ==============================
# 🎯 SECTION 3: RAG IMPORTS
# ==============================

# RAG imports
import chromadb
from chromadb.utils import embedding_functions

# Gemini imports
import google.generativeai as genai
from dotenv import load_dotenv

# ==============================
# 🎯 SECTION 4: Setup & Configuration
# ==============================

load_dotenv()

app = Flask(__name__)
CORS(app)

# Paths
UPLOAD_FOLDER = "uploads"
CHROMA_PATH = "chroma_db"
ALLOWED_EXTENSIONS = {'txt', 'md', 'pdf'}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(CHROMA_PATH, exist_ok=True)

# API Key
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("❌ ERROR: GEMINI_API_KEY not found in .env file!")
    USE_GEMINI = False
else:
    genai.configure(api_key=api_key)
    print("✅ Gemini API configured successfully")
    USE_GEMINI = True

# Model setup
GEMINI_MODEL = "gemini-2.0-flash-exp"
DEBUG_STREAMING = True
CHUNK_SIZE = 500

# Initialize ChromaDB
chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)

# Embedding function
embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

print("\n" + "="*50)
print("🔧 ChromaDB Initialized")
print(f"📁 Upload folder: {UPLOAD_FOLDER}")
print(f"💾 ChromaDB path: {CHROMA_PATH}")
print("="*50)


# ==============================
# 📁 SECTION 5: HELPER FUNCTIONS
# ==============================

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def chunk_text(text, chunk_size=CHUNK_SIZE):
    """Split text into chunks"""
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunk = text[i:i+chunk_size]
        if chunk.strip():
            chunks.append(chunk)
    return chunks

def extract_text_from_pdf(filepath):
    """Extract text from PDF file"""
    if not PDF_SUPPORT:
        raise Exception("PDF support not installed. Run: pip install pypdf")
    
    try:
        reader = PdfReader(filepath)
        text = ""
        
        for page_num, page in enumerate(reader.pages):
            page_text = page.extract_text()
            if page_text:
                text += f"\n--- Page {page_num + 1} ---\n"
                text += page_text
        
        if not text.strip():
            raise Exception("No text could be extracted from PDF")
        
        print(f"   📄 Extracted {len(text)} characters from {len(reader.pages)} pages")
        return text
    
    except Exception as e:
        raise Exception(f"PDF extraction failed: {str(e)}")

def read_file_content(filepath, filename):
    """Read content from file (supports .txt, .md, .pdf)"""
    file_ext = filename.rsplit('.', 1)[1].lower()
    
    if file_ext == 'pdf':
        return extract_text_from_pdf(filepath)
    else:
        # Text files
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()