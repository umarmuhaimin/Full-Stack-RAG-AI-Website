# ==============================
# SECTION 1: IMPORTS
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
# SECTION 2: PDF HANDLING
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
# SECTION 3: RAG IMPORTS
# ==============================

# RAG imports
import chromadb
from chromadb.utils import embedding_functions

# Gemini imports
import google.generativeai as genai
from dotenv import load_dotenv