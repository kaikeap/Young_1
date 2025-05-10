class contaBancaria():
    def __init__(self):
        self.titular = input("Qual o nome da pessoa: \n")
        self.saldo = int(input("você tem: \n"))

    def depositar(self):
        self.depositarDinheiro = int(input("Qual o valor que deseja depositar? \n"))
        self.depositarDinheiro += self.saldo
    
    def sacar(self):
        self.sacarDinheiro = int(input("Qual o valor que deseja sacar? \n"))
        self.sacarDinheiro += self.saldo

    def ver_saldo(self):
        return f"Seu saldo é de {self.saldo}"
    
contaBancaria()

print('digite um 1 para depositar' \
'2 para sacar' \
'3 ver saldo')

while True:
    variavel = int(input())
    
    if variavel == 1:
        contaBancaria.depositar
        break

    elif variavel == 2:
        contaBancaria.sacar
        break

    elif variavel == 3:
        contaBancaria.ver_saldo
        break

#     1. Crie uma classe chamada Pessoa

# Atributos: nome, idade

# Método: apresentar() que imprime "Olá, meu nome é X e tenho Y anos".
# ----------------------------------------------------------------------
# 2. Crie uma classe chamada Retangulo

# Atributos: largura, altura

# Método: area() que retorna a área do retângulo.

# Crie um objeto e mostre a área.
# ----------------------------------------------------------------------
# 3. Classe Carro com velocidade

# Atributos: marca, velocidade

# Método: acelerar(valor) que aumenta a velocidade.

# Método: frear(valor) que diminui a velocidade.

# Mostre a velocidade atual após cada chamada.
# ----------------------------------------------------------------------
# 4. Classe ContaBancaria

# Atributos: titular, saldo

# Métodos: depositar(valor), sacar(valor), ver_saldo()

# Teste os métodos com um objeto.
# ----------------------------------------------------------------------
# 5. Classe Aluno com notas

# Atributos: nome, nota1, nota2

# Método: media() que calcula a média das duas notas.

# Método: aprovado() que retorna True se a média for >= 6.
# ----------------------------------------------------------------------
# 6. Classe Livro

# Atributos: titulo, autor, paginas

# Método: detalhes() que imprime todas as informações do livro.
# ----------------------------------------------------------------------
# 7. Classe Cachorro com comportamento

# Atributos: nome, raca

# Métodos: latir(), que imprime “Au au!”, e apresentar(), que mostra nome e raça.
# ----------------------------------------------------------------------
# 8. Classe Calculadora

# Métodos: somar(a, b), subtrair(a, b), multiplicar(a, b), dividir(a, b)

# Crie um objeto e teste todos os métodos com diferentes valores.
# ----------------------------------------------------------------------
# 9. Classe Produto com desconto

# Atributos: nome, preco

# Método: aplicar_desconto(porcentagem) que altera o preço com base no desconto.

# Mostre o preço antes e depois.
# ----------------------------------------------------------------------
# 10. Classe Agenda com contatos

# Atributo: contatos (lista)

# Métodos: adicionar_contato(nome), remover_contato(nome), listar_contatos()

# Crie uma agenda, adicione e remova contatos e exiba a lista.