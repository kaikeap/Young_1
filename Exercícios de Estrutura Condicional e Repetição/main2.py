import random

bot = random.randint(1, 100)

user = int(input('tente adivinhar um numero de 1 a 100\n'))

while user != bot:
    if user < bot:
        print('esse numero é menor que o bot')
    elif user > bot:
        print('esse numero é maior que bot')
    user = int(input('tente adivinhar um numero de 1 a 100\n'))

