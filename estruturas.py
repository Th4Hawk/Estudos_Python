# Declara uma variavel do tipo int
numero = 20
# Estruturas condicionais (condição)
# Obs -> O python não possue switch
if numero == 20:
    print("Numero é igual a 20")
elif numero == 15:
    print("Numero é igual a 15")
else:
    print("Numero não é igual a 15 nem a 20")

# Condição usando operadores de identidade
# is -> Verifica se as duas variaveis possuem o mesmo objeto
# is not -> Verifica se as duas variaveis não possuem o mesmo objeto
variavel1 = [13,22,17]
variavel2 = [13,22,17]

if variavel1 is variavel2:
    print("As variaveis são o mesmo objeto")
else:
    print("As variaveis não são o mesmo objeto")

# Condição usando operadores de associação 
# in -> Verifica se um valor esta presente em uma sequencia
# not in -> Verifica se um valor não esta presente em uma sequencia
lista = [4,2,5]

if 4 in lista: 
    print("O numero 4 esta presente na lista")
else:
    print("O numero 4 não esta preente na lista")

# Estruturas de controle de loop
# while -> Executa um bloco de codigo desde que a condição seja verdadeira
# for -> Executa um bloco de codigo iterando sobre uma sequencia 

# Usando for (o range gera uma sequencia de numeros)
print("Resultados do loop for")
for i in range(5):
    print(i)

# Usando while 
contador = 0
print("Resultados do loop while")
while contador < 5:
    print(contador)
    contador += 1

# Estruturas de controle de loop
# break -> Para a execução do loop 
# continue -> Pula para a proxima iteração do loop
