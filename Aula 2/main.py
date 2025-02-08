# # print('ex 1')
# # numero = int(input('digite um numero: '))
# # if numero % 2 == 0:
# #     print('par')
# # else:
# #     print('impar')
# # print('fim')

# print('ex 2')
# numero = int(input('digite um numero: '))

# if numero > 0:
#     print('positivo')
# elif numero < 0:
#     print('negativo')
# else:
#     print('zero')
# print('fim')print('ex 4')numberone = int(input('digite um numero de 0 a 10: '))if numberone >= 6 and numberone <= 10:    print('Aprovado')elif numberone < 0 or numberone > 10:    print('erro')else:    print('reprovado')print('ex 5')num = int(input('digite um numero de 1 a 7: \n'))if num == 1:    print('segunda-feira')elif num == 2:    print('terça-feira')elif num == 3:    print('quarta-feira')elif num == 4:    print('quita-feira')elif num == 5:    print('sexta-feira')elif num == 6:    print('sabado')elif num == 7:    print('domingo')elif num > 7 or num < 1:    print(f'{num} esse dia n existe')

print('ex 7')

import randow 

num_randow = randow.radint(1,10)

num = 0

while(num != num_randow):
    num = int(input('digite um número entre 1 e 10: '))
    if(num == num_randow):
        print('parabéns')