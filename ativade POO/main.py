class pessoa():
    def __init__(self):
        self.nome = input("digite seu nome: \n")
        self.idade = input("digite sua idade: \n")
    
    def apresentar(self):
        return f"Ola , meu nome é {self.nome}, eu tenho {self.idade} anos"
    
pessoa1 = pessoa()

print(pessoa1.apresentar())




