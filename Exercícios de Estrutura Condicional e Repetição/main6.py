num = int(input('digite um numero\n'))

total = 0

for i in range(1, num + 1):
    if num % i == 0:
        print(f'Divisor: {i}')
        total += 1

print(f'total de divisores = {total}')
