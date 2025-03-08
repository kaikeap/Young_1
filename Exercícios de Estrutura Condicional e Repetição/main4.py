
continuar = 's'

while continuar == 's':
    for i in range(10, -1, -1):
        print(i)
        if i != 0:
            tempo_restante = i - 1
            print(f'{tempo_restante} é o tempo que falta ')
        else:
            print('Feliz ano novo!!!')
            continuar = input('reiniciar s/n ')
