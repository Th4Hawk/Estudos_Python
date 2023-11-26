## Anotações uteis.

Um método é uma ação que pode ser executada em determinado dado. Exemplo:

```py
nome = "dark side"
# Chama o método.title()
print(nome.title())
```

Removendo espaços em branco:
```py
nome = " Oi "
# Remove o espaço em branco do lado direito
print(nome.rstrip())
# Remove o espaço em branco do lado esquerdo
print(nome.lstrip())
# Remove o espaço em branco dos dois lados
print(nome.strip())
```

Representa valores que não são strings como string
```py
dia = 10
# A função str() é chamada para representar o inteiro como uma string
print("Hoje é dia " + str(dia))
```