class Animal:
    def __init__(self, nome, peso):
        self.nome = nome
        self.peso = peso
        self.velocidade = 0 
    def emitir_som(self):
        raise NotImplementedError("Subclasse deve implementar este método")

    def correr(self):
        self.peso-=1
        self.velocidade +=1
    
    def velocidade_atual(self):
        return self.velocidade
    def comer(self):
        self.peso +=1
    def mostra_peso(self):
        return self.peso
    def __str__(self):
        return f"Eu sou um animal chamado {self.nome}"
