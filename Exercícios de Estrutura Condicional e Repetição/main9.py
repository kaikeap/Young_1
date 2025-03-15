while True:
    print('quer verificar Políndro? (s/n) ')
    escolha = input()
    if escolha.lower() == 's':
        print('digite a palavra  para verificar políndro: ')
        frase = input()
        invertida = frase [::-1]
        if invertida == frase:
            print('é palíndromo')
        else:
            print('não é palíndromo')
