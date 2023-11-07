import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.util import ngrams
from nltk.metrics.distance import jaccard_distance
import random
import os 
import json 

def get_sugestoes(pergunta_usuario, res: list):
    arquivoPerguntas = "perguntas.json"
    arquivoRespostas = "respostas.json"

    CAMINHO_ABSOLUTO_PERGUNTAS  = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            arquivoPerguntas,
        )
    )

    CAMINHO_ABSOLUTO_RESPOSTAS  = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            arquivoRespostas,
        )
    )

    with open(CAMINHO_ABSOLUTO_PERGUNTAS, 'r') as arquivo:
        perguntas = json.load(arquivo)

    with open(CAMINHO_ABSOLUTO_RESPOSTAS, 'r') as arquivo:
        respostas = json.load(arquivo)


    # Baixar os recursos necessários do NLTK (apenas uma vez)
    nltk.download('punkt')
    nltk.download('stopwords')

    # Obter sugestões de respostas
    sugestoes = obter_sugestoes(pergunta_usuario, perguntas, respostas)
    tam_sugestao = 1

    # Exibir as sugestões

    while True:
        s = random.choice(sugestoes[0])
        if s not in res:
            res.append(s)
            break

# Função para calcular a similaridade Jaccard entre duas frases
def calcular_similaridade_jaccard(frase1, frase2):
    tokens_frase1 = set(word_tokenize(frase1.lower()))
    tokens_frase2 = set(word_tokenize(frase2.lower()))
    return 1 - jaccard_distance(tokens_frase1, tokens_frase2)

# Função para obter sugestões de respostas
def obter_sugestoes(pergunta, perguntas, respostas, num_sugestoes=1):
    sugestoes = []
    for p, r in zip(perguntas, respostas):
        similaridade = calcular_similaridade_jaccard(pergunta, p)
        #print(similaridade, r)
        sugestoes.append((r, similaridade))
    #print(sugestoes)


    sugestoes = sorted(sugestoes, key=lambda x: x[1], reverse=True)[:num_sugestoes]

    return [sugestao[0] for sugestao in sugestoes]