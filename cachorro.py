from animal import Animal

class Cachorro(Animal):
    def __init__(self, nome, raca, peso):
        super().__init__(nome, peso)
        self.raca = raca

    def emitir_som(self):
        return f"{self.nome} auau!"

    def correr(self):
        self.peso -= 0.2
        self.velocidade += 10

    def mostra_peso(self):
        return self.peso

    def __str__(self):
        return f"Eu sou um cachorro da raça {self.raca}, meu nome é {self.nome}"
