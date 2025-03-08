def fatorial():
    num = int(input('digite um numero'))

    for i in  range(num -1, 0, -1):
        num = num * i
        print(num, end= ' ')

while True:
    fatorial()
    resposta = (input('deseja fatorar mais algum numero? (s/n): '))
    if resposta != 's':
        print('encerrado o programa...')
        break