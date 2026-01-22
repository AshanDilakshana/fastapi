import sys
import os
from pathlib import Path

# Add the parent directory to sys.path so we can import from main.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from main import app

# Vercel needs the app object to be available at the top level
# of the file specified in vercel.json
