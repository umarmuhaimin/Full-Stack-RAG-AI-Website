# ⚙️ FOUNDATION MODE — Setting Up the Virtual Environment

We don’t install packages globally like beginners.

We isolate everything — like real engineers.

Let’s initialize our virtual environment (venv) properly ⬇️

---------------------------------------------------------------------------------------------

**📁 Step 1 — Set Up the Project Folder**

Before writing any code, let’s create a clean workspace for this AI project.

Open your terminal and run the following:

*# Go to your Desktop (or any location you prefer)*
cd ~/Desktop

*# Create a new folder for this project*
mkdir Full-Stack-RAG-AI-Website

*# Enter the project folder*
cd Full-Stack-RAG-AI-Website

---------------------------------------------------------------------------------------------
✅ This ensures everything stays organized and isolated

✅ Avoids messy file management later

✅ You are now officially at Ground Zero — the clean start every serious developer should have

---------------------------------------------------------------------------------------------

*📁 STEP 2 — Create a Virtual Environment (venv)*

# Create venv
python3 -m venv venv

This creates a sandboxed Python environment so nothing interferes with your global system. Clean & professional.


*📁 STEP 3 — Activate the Environment*

# Activate venv
source venv/bin/activate

Once activated, your terminal should now show:
(venv) yourname@MacBook Full-Stack-RAG-AI-Website %

✅ If you see (venv) — congratulations, you're inside your AI lab.


*📁 STEP 4 — Upgrade pip (Important for Stability)*

# Upgrade pip inside venv
pip install --upgrade pip

This ensures we’re not using a Stone Age version of pip. Always do this first.


*📁 STEP 5 — Install Core Dependencies*

# Install packages (now they go into venv!)
pip install flask flask-cors pypdf PyPDF2

Wait for installation...
These are essential backend tools — server, security, and PDF processing.


*📁 STEP 6 — Confirm Installation (Optional but Smart)*

# Check installed packages
pip list

You should see:
→ Flask
→ flask-cors
→ pypdf
→ PyPDF2
→ Werkzeug (auto-installed by Flask)


*📁 STEP 7 — Create Your Backend Entry Point*

# Create empty backend.py
touch backend.py

We now officially have a starting point for the AI engine.


*📁 STEP 8 — Open the Project in VS Code Properly*

# Open VS Code from this activated venv terminal code .
code .

IMPORTANT: Make sure you do this from inside the activated venv terminal,
so VS Code auto-detects your environment. Zero headaches later.


*📁 STEP 9 — Confirm Python Interpreter in VS Code*

Inside VS Code:

1. Press Cmd + Shift + P
2. Search → Python: Select Interpreter
3. Choose the one that says ./venv/bin/python or ('venv': venv)

✅ Bottom-right corner should now show:
🐍 Python 3.x.x ('venv': venv)

#############################################################################################
✅ FOUNDATION SECURED

You didn’t just “install Python” —
You set up a real developer environment the way professionals do.

From here onward, you’re no longer learning AI —
you’re building AI.
