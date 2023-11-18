## Asyncio

O asyncio é uma biblioteca que fornece uma estrutura para escrever código assíncrono baseado em corrotinas, que são funções especiais que podem ser suspensas e retomadas durante a execução. Ele é útil em atividades que precisam lidar com muitas operações de entrada/saída de dados.

### Conceitos chave

1 - Corrotinas

As funções assíncronas são chamadas de corrotinas e são definidas pela palavra-chave `async def`

Exemplo:

```py
# Importa a biblioteca asyncio 
import asyncio

# Cria uma função assíncrona usando a palavra-chave async def
async def teste():
    # Mostra "Iniciando corrotina" no console
    print("Iniciando corrotina")
    # O await é usado para esperar que outra corrotina seja concluida antes de continuar a execução do codigo
    # Suspende a execução da proxima tarefa por 2 segundos
    await asyncio.sleep(2)
    # Mostra "Corrotina finalizada" no console
    print("Corrotina finalizada")

```

2 - Await

A palavra-chave await é usada para esperar que outra corrotina seja concluída antes de continuar a execução do código.

3 - Funções assíncronas e funções não assíncronas

As funções assíncronas podem chamar funções assíncronas e não assíncronas, porem, funções não assíncronas não podem chamar diretamente funções assíncronas, por isso usamos o `await`

### Util

1 - `asyncio.run()`

O asyncio.run configura e executa um programa de forma assíncrona.


