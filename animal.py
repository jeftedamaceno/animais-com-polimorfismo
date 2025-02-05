class Animal:
    def __init__(self, nome):
        self.nome = nome
        self.velocidade = 0
    def emitir_som(self):
        raise NotImplementedError("Subclasse deve implementar este método")

    def correr(self):
        self.velocidade +=1
    def velocidade_atual(self):
        return self.velocidade
    def __str__(self):
        return f"Eu sou um animal chamado {self.nome}"
