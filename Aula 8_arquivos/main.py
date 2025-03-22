def adcionar_filme():
    with open('filmes.txt', 'a' , encoding='utf-8') as arquivo:
        while True:
            filme = input ('Digite nome do filme (ou '' sair ''):')

            if filme.lower() == ' sair':
                break

            arquivo.write(filme + '\n')
            print(f'Filme {filme} adicionado com sucesso!')

def ler_filmes():
    with open('filme.txt', 'r' , encoding='utf-8') as arquivo :
        filme  = arquivo.read()
        print(filme)

while True:
    print('**********************')
    print('        filmes        ')
    print('**********************')
    print('1- Digitar filme')
    print('2- ler filmes')
    print('3- sair')
    print('**********************')
    opcao =  int(input('Opção Desejada: '))
    if opcao == 1:
        adcionar_filme()
    elif opcao  == 2