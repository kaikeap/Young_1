class contaBancaria():
    def __init__ (self, titular, saldo = 100):
        self.saldo = saldo
        self.titular = titular

    def depositar(self,valor):
        self.saldo += valor
        print(f'você depositou {valor} agora você tem {self.saldo}')

    def sacar(self,valor):
        self.saldo -= valor
        print(f"você retirou {valor} e agora tem {self.saldo}")

    def ver_saldo(self):
        print(f'você tem {self.saldo}')

minhaConta = contaBancaria('Kaike')

minhaConta.depositar(100)
minhaConta.sacar(30)
minhaConta.ver_saldo()
        