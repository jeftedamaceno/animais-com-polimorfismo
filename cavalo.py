from animal import Animal

class Cavalo(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)
        self.raca = raca

    def emitir_som(self):
        return f"{self.nome} relincha!"
    def correr(self):
        self.velocidade += 20
        print(f'velocidade atual {self.velocidade}')
    def __str__(self):
        return f"Eu sou um cavalo da raça {self.raca}, meu nome é {self.nome}"