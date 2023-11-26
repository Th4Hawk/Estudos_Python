# Criando uma lista
lista = ['elemento1', 'elemento2', 'elemento3', 'elemento4']
# Acessando todos os elementos da lista
print(lista)
# Acessando um determinado elemento
print(lista[0])
# Manipulando o elemento
print(lista[0].title())
# Modificando o elemento
lista[0] = 'novoelemento'
print(lista)
# Adicionando um elemento
lista.append("novoelemento2")
print(lista)
# Removendo um elemento
del lista[0]
# Usando o metodo pop
elemento_removido = lista.pop()
print(lista)
print(elemento_removido)
# Usando o metodo remove
lista.remove('elemento2')
print(lista)
