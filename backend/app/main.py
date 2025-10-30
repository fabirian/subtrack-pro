from fastapi import FastAPI
from fasapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Backend is running correctly 🚀"}
