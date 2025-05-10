
class carro():
    def __init__ (self):
        self.velocidade = int(input("O carro esta a: \n"))
        self.marca = input("Qual a marca do carro: \n")

    def acelerar(self):
        self.valor = self.velocidade + 10
        return f"o carro eta a km{self.valor}/h"
    
    def frear(self):
        self.valor2 = self.velocidade - 5
        return f"o carro eta a km{self.valor2}/h"
    
dirigir = carro()

print(dirigir.acelerar(),dirigir.frear())

