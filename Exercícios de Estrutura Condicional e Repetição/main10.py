while True:
    frase = input('digite uma frase: ')
    caracter = input('digite o caracter que deseja contar: ')
    if len(caracter) != 1:
        print('digite apenas um caractere')
        continue
    else:
        cont = frase.count(caracter)
        print(f'O caractere {caracter}, aparece {cont} vezes')
        if input('contar outro (s/n) ').lower() != "s":
            break