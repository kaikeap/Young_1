class produto_com_desconto():
    def __init__(self,nome,preco):
        self.name = nome
        self.dinheiro = preco

    def AplicarDesconto(self):
        while True:
            self.valor = float(input("Qual o valor do desconto? (!obrigatorio ser número com . (ex: 0.20)!)\n"))
            if self.valor > 1 or self.valor < 0:
                print("o desconto me parece um pouco alto poderia repitir")
            else:
                self.macaco = self.valor * self.dinheiro
                print(f"O desconto é de:{self.macaco}")
                break
        
    
    def valorDoProduto(self):
        return f"O valor do produto ficou: {self.macaco - self.dinheiro}"
    
    def VaiSer(self):
        while True:
            self.Cartão = input("(atendente): Debito ou Credito\n")
            if self.Cartão == "debito":
                print("(pi,pi,pi) Cartão recusado >:\n")
            elif self.Cartão == "credito":
                print("(pi,pi,pi) pagamento concluido (:\n")
                break
        

loja = produto_com_desconto("Desintupidor", 50)

print(loja.AplicarDesconto())
print(loja.valorDoProduto())
print(loja.VaiSer())

