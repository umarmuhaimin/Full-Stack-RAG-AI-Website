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