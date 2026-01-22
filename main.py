# main.py
from src.app.api import app  # your FastAPI instance

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)
