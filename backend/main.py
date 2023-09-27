from fastapi import FastAPI
from utils.nltk import greeting

app = FastAPI()

@app.get("/")
async def root():
    gr = greeting("Rafa")
    return { "message": gr }