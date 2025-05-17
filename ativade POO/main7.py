class Cachorro():
    def __init__(self, nome, raca):
        self.nome=nome
        self.raca=raca

    def Latir (self):
        return 'au au'
    
    def apresentar(self):
        return f'Raça: {self.raca} \nNome: {self.nome}'
    
cachorro1 = Cachorro('Charlie' , 'Bace')

print(cachorro1.Latir())
print(cachorro1.apresentar())