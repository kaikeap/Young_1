notas = []
resposta = ''
i = 1
while resposta != 'n':
    nota = float(input(f'digite nota {i}: '))

    notas.append(nota)
    resposta = input('deseja digitar mais alguma nota? (s/n) ')
    i = i +1

total = sum(notas) / len(notas)

print(total)

if total >= 7:
    print(F'aprovado{total}')
elif total <= 4:
    print(f'reprovado com nota {total}')
else:
    print(f'recuperação com nota {total}')
