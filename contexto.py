# O gerenciamento de contexto é importante para lidar com recursos que precisam ser inicializados e finalizados. 
# Usamos a palavra "with" para trabalhar com contexto 
# Para um objeto ter suporte ao contexto é necessario que ele implemente os seguintes metodos
# __enter__ -> Esse metodo deve ser chamado quando a execução do bloco "with" é iniciada
# __exit__ -> Esse metodo deve ser chamado quando a execução do bloco "with" é concluida

# Exemplo de gerenciamento de contexto 
with open("oi.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
