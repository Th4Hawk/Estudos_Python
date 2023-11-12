# Importa a classe "FastAPI" do framework fastapi 
from fastapi import FastAPI

# Cria uma instancia da classe e a nomeia de "app" 
app = FastAPI()

# Define um "decorador" que recebe '/' 
@app.get('/')
# Função assíncrona no qual o "decorador" acima processa
async def boas_vindas():
    return {"message": "bem vindo!"}

# Define um "decorador" que recebe '/nome/{nome}' e tem como parametro {nome}
@app.get('/nome/{nome}')
# Função assíncrona no qual o "decorador" acima processa
# A função recebe o parametro "nome" e retorna um json informando o nome recebido
async def nome(nome):
    return {"nome": nome}


