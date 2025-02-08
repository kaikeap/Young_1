print('ex 6')

numberone = int(input('digite um numero\n'))

numbertwo = int(input('digite um numero\n'))

numberthree = int(input('digite um numero\n'))

if numberone > numbertwo and numberone > numberthree:
    print(f'{numberone} é maior que {numbertwo} e {numberthree}')

elif numbertwo > numberone and numbertwo > numberthree:
    print(f'{numbertwo} é maior que {numberone} e {numberthree}')

elif numberthree > numberone and  numberthree > numbertwo:
    print(f'{numberthree} é maior que {numbertwo} e {numberone}')
---------------------------------------------------------------
    print('ex 7')

import randow 

num_randow = randow.radint(1,10)

num = 0

while(num != num_randow):
    num = int(input('digite um número entre 1 e 10: '))
    if(num == num_randow):
        print('parabéns')