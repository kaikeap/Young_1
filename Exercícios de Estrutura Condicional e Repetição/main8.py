base = int(input('digite a base\n'))
expoente = int(input('digite o expoente\n'))


for i in range(1,expoente):
    base *= base
    print(base, end= ' ')
