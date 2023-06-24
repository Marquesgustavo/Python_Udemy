#Aula sobre Self em classe Python
#Carro é a Classe
#acelerar é o método

class Carro:
    def __init__(self,nome):
        self.nome = nome
    
    def acelerar(self):
        print(f'{self.nome} está acelerando...')

fusca = Carro('Fusca')
fusca.acelerar() # 1 opção
Carro.acelerar(fusca)  # 2 opção

celta = Carro(nome='Celta')
celta.acelerar()
Carro.acelerar(celta)