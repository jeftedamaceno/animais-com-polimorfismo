from animal import Animal

class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)
        self.raca = raca

    def emitir_som(self):
        return f"{self.nome} diz: Au Au!"
    def correr(self):
        self.velocidade += 5
        print(f'velocidade atual {self.velocidade}')
    def __str__(self):
        return f"Eu sou um cachorro da raça {self.raca}, meu nome é {self.nome}"