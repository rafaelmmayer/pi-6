from fastapi import FastAPI
from lib.nltk import greeting

app = FastAPI()

@app.get("/")
async def root():
    gr = greeting("Rafa")
    return { "message": gr }