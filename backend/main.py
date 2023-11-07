from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  
from utils.nltk import get_message
from utils.IA import get_sugestoes
import threading

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
async def root(frase: str, num_sugestoes = '3'):

    num_sugestoes = int(num_sugestoes)

    res = []
    threads = []

    for i in range(num_sugestoes):
        t = threading.Thread(target=get_sugestoes, args=(frase, res))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    return { "sugestoes": res }