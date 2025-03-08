## notas = []
## i = 1
## 
## while True:
##     nota = float(input(f'Digite a nota {i}: '))
##     if nota >= 0 and nota <=  10:
##         notas.append(nota)
##     else:
##         print('A nota deve estar entre 0 e 10')
##         continue
##     continuar = input('Deseja inserir mais uma nota? (s/n): ')
##     if continuar != 's':
##         media = sum(notas) / len(notas)
##         print(media)
    
notas = [3, 5, 7]

continuar = ('s')

for i in notas:

    while continuar == 's':

        if i < 4 and i >= 0:
           print(f'{i} reprovado')

        elif i >= 4 and i < 7:
            print(f'{i} recuperação')

        elif i >= 7 and i < 10:
            print (f'{i} aprovado')
            
            continue
        continuar = input('cotinuar com as notas? s/n ')
        if continuar != 's':
            print('essas foram as notas')
            break
