# TODO: Melhorar as anotações relacionadas a POO

# Classe
# As classes são como um plano que podem ser usadas para definir atributos (variaveis) e metodos (funções) de um objeto
class Moto:
    def __init__(self, modelo, cor):
        self.modelo = modelo
        self.cor = cor 

    def acelelar(self):
        print(f"A moto de cor {self.cor} de modelo {self.modelo} esta acelerando!")

# Objeto
# Os objetos são instancias de uma classe, ela possui as caracteristicas da classe que pertence
minha_moto = Moto("honda", "preta")
# Chamando o metodo "acelelar" que esta presente na classe 
minha_moto.acelelar()
