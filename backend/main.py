from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  
from utils.nltk import greeting

app = FastAPI()

origins = [
    'http://localhost:5173'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.get("/")
async def root(frase: str):
    
    return { "message": frase }