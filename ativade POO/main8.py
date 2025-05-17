class calculadora():
    def somar(self,valor1,valor2):
        return valor1 + valor2    
    
    def subtrair(self,valor1,valor2):
        return valor1 - valor2
    
    def multiplicar(self,valor1,valor2):
        return valor1 * valor2    
    
    def dividir(self,valor1,valor2):
        return valor1 / valor2
    
calculadora1 = calculadora()

print(calculadora1.somar(5,5))
print(calculadora1.subtrair(5,5))
print(calculadora1.multiplicar(5,5))
print(calculadora1.dividir(5,5))