from fastapi import FastAPI

# Debugging Vercel 500 Error
# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# from src.app.api import app

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World from minimal FastAPI"}

@app.get("/{path:path}")
def catch_all(path: str):
    return {"message": f"Cached {path}"}
