print('ex 9')

numero = int(input('digite um numero: \n'))

if numero <= 25 and numero >= 0:
    print('1° intervalo')

elif numero <= 50 and numero >= 26:
    print('2° intervalo')

elif numero <= 75 and numero >= 51:
    print('3° intervalo')

elif numero <= 100 and numero >= 76:
    print('intervalo fimal')

else:
    print('fora do intervalo')