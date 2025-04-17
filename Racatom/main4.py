import main
import main2
import main3

notas = []

print('Esse site foi feito por "Kaike Aparecido" e "Julho Ferreiera" com o objetivo de você analisar três jogos pouco conhecidos e determinar qual sera oi melhor em sua opnião, talvez até despertando curiosidade na pessoa de jogar')

while True:
    print('_______________MENU_________________')
    print('====== (1) Analisar o game1 ========')
    print('====== (2) Analisar o game2 ========')
    print('====== (3) Analisar o game3 ========')
    print('____________________________________')
    jogo = int(input('Qual jogo você deseja analisar?\n'))
    if jogo == 1:
        main.game1()
        nota_final = int(input('Confirme a nota dada redigitando a nota\n'))
        notas.append(nota_final)
    elif jogo == 2:
        main2.game2()
        nota_final = int(input('Confirme a nota dada redigitando a nota\n'))
        notas.append(nota_final)
    elif jogo == 3:
        main3.game3()
        nota_final = int(input('Confirme a nota dada redigitando a nota\n'))
        notas.append(nota_final)