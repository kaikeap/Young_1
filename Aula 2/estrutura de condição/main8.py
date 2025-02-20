print('ex 8')

number = int(input('digite sua idade'))

if number < 18 and number >= 0:
    print('menor de idade')

elif number >= 18 and number <= 64:
    print('adulto')

elif number >= 65:
    print('idoso')

else:
    print('você é inexistente, pare de graça')