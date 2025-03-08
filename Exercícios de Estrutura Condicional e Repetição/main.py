num = int(input('digite um numero'))

for i in  range(num, 1, -1):
    num *= i
    print(num)