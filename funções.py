# Para declarar uma função usamos a palavra chave "def"
# A estrutura de uma função é a seguinte:
# nome -> É o nome que iremos dar a função 
# parâmetros -> São os parametros que a função vai receber (opcional)
# corpo da função -> São as intruções que irão ser executadas quando a função é chamada
# return -> É a palavra-chave usada para devolver o resultado da execução da função (opcinal)
def boas_vindas(nome="visitante"):
    return f"Olá {nome}"

# Declarando uma variavel do tipo string
nome = "thomas"
# Executando a função e passando como parametro a variavel
print(boas_vindas(nome))
