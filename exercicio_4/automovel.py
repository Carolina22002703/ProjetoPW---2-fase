class Automovel:
    def __init__(self, cap_dep, quant_comb, consumo):
        self.capacidade = cap_dep
        self.quantidade = quant_comb
        self.consumo = consumo
    
    def devolve_combustivel(self):
        return f'Quantidade de combustível: {self.quantidade}'

    def devolve_automonia(self):
        return f'Autonomia do automóvel: {(self.quantidade*100)/self.consumo}'
    
    def devolve_abastece(self, litros):
        self.quantidade += litros
        if(self.quantidade > self.capacidade):
            self.quantidade -= litros
            return ('Erro')
        else:
            return f'Autonomia do automóvel depois do abastecimento: {(self.quantidade*100)/self.consumo}'

    def devolve_percorre(self, km):
        autonomia = (self.quantidade*100)/self.consumo
        diferenca = autonomia - km
        if(diferenca > 0):
            return f'Autonomia do automóvel depois de percorrer {km}: {diferenca}'
        else:
            return 'Erro'
        

#Chamar funções
carro = Automovel(60,10,15)
print(carro.devolve_combustivel())
print(carro.devolve_automonia())
print(carro.devolve_abastece(45))
print(carro.devolve_abastece(60)) #Testar a condição de erro
print(carro.devolve_percorre(150))
print(carro.devolve_percorre(400)) #Testar a condição de erro