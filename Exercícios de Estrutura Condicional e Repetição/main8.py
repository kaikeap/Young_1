while True:
    b = int(input('digite a base: '))
    e = int(input('digite o expoente: '))
    r = b**e
    print(r)
    sair = input('deseja sair? ')
    if sair.lower() == 'sair':
        break