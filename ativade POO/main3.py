
class carro():
    def __init__ (self, velocidade1):
        self.velocidade = velocidade1
        self.marca = input("Qual a marca do carro: \n")

    def acelerar(self, valor):
        self.velocidade += valor
        print( f"o carro esta a km{self.velocidade}/h")
    
    def frear(self,valor):
        self.velocidade -= valor
        print( f"o carro esta a km{self.velocidade}/h")
    
dirigir = carro(100)

dirigir.acelerar(30)
dirigir.acelerar(30)
dirigir.frear(10)
dirigir.frear(30)
