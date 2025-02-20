print('ex 7')

import randow

num_randow = randow.radint(1,10)

num = 0

while(num != num_randow):
    num = int(input('digite um número entre 1 e 10: '))
    if num == num_randow:
        print('parabéns')