## Variaveis

O python é uma linguagem de tipagem dinâmica, ou seja, não é necessário especificar o tipo da variável de forma explicita.

Tipos de dados:

```py
inteiro = 10
ponto_flutuante = 0.17
string = "Oi"
booleano = True
```

Também é possível realizar operações com variáveis.

```
a = 5 
b = 10 
soma = a + b 
subtração = b - a
multiplicação = b * a 
divisão = b / a 
```

Também é possível criar variáveis locais, globais e constantes.

```py
# Variável constante, que não pode ser modificada
# Para uma variável ser constante, é necessário que seu nome seja maiúsculo
VARIAVEL_CONSTANTE = 30

# Esta é uma variável global, que pode ser acessada por todo o programa
variavel_global = 20

def oi():
    # A variável só pode ser acessada no escopo da função, logo, ela é uma variável local
    variavel_local = 10
    print(variavel_local)

oi()
print(variavel_global)
```

### Manipulando strings

```py
nome = "Banana"
# Deixa a string com letras maiúsculas
print(nome.upper())
# Deixa a string com letras minúsculas
print(nome.lower())
```

### Regras importantes

1 - Não é permitido que nomes de variaveis tenham espaço. Exemplo:

```py
# Permitido
nome_legal = "dog"
# Não é permitido
nome legal = "dog"
```

2 - Não é permitido que nomes de variaveis comecem com numeros. Exemplo:

```py
# É permitido
variavel_1 = 1
# Não é permitido
1_variavel = 1
```

3 - Não é permitido usar palavras reservadas do python como nome de variavel. Exemplo:

```py
# Não é permitido
print = "a"
```