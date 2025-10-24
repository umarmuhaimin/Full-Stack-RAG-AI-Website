# 🧠 SYSTEM BOOT — Initializing Backend & Enabling PDF Support

Preparing essential backend tools and ensuring the system is ready to safely handle PDF inputs.

---------------------------------------------------------------------------------------------

**✅ SECTION 1: IMPORTS (Lines 1–12) → We start by importing all required tools for our backend.**

**Step 1: Import Flask — allows this file to act as the backend server (Flask, request, Response, etc.)**

from flask import Flask, request, Response, stream_with_context, jsonify

**Step 2: Enable CORS — so the frontend website can communicate with the backend without browser security issues.**

from flask_cors import CORS

**Step 3: Import Python utilities (os, json, time) — used for file handling, JSON formatting, and timing functions.**

import os

import json

import time

**Step 4: Import secure_filename — protects against unsafe filenames during file uploads (security protection).**

from werkzeug.utils import secure_filename

**Step 5: Import Path — for clean and safe file path handling.**

from pathlib import Path

**Step 6: Import datetime tools — useful for logging, timestamps, or scheduling features later.**

from datetime import datetime, timedelta

---------------------------------------------------------------------------------------------

**✅ SECTION 2: PDF HANDLING (Lines 14–26) → We check whether PDF file support is available.**

**Step 1: Try importing pypdf — the recommended modern library for reading PDFs.**

try:

    from pypdf import PdfReader

    PDF_SUPPORT = True

    print("✅ PDF support enabled (pypdf)")

**Step 2: If it’s not available, try importing PyPDF2 instead.**

except ImportError:

    try:
    
        from PyPDF2 import PdfReader

        PDF_SUPPORT = True

        print("✅ PDF support enabled (PyPDF2)")

**Step 3: If neither library exists — disable PDF support and notify the user via a warning message.**

except ImportError:

        PDF_SUPPORT = False

        print("⚠️  PDF support disabled (install: pip install pypdf)")

**Step 4: Print a status message (success or warning) so the developer immediately knows if PDF support is active.**

print("✅ PDF support enabled (pypdf)")

print("✅ PDF support enabled (PyPDF2)")

print("⚠️  PDF support disabled (install: pip install pypdf)")