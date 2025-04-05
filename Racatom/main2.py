def game2():
    while True:
        print("Shaterred Pixel Dungeon")
        print('_______________________________________')
        print('===== (1) tempo gasto e ano de criação=')
        print('===== (2) dinheiro gasto===============')
        print('===== (3) pessoas da equipe============')
        print('===== (4) arte,historia e gameplay=====')
        print('_______________________________________')
        analisar = input('O que pretende analizar ?\n')
        if analisar == '1':
            print('O jogo começou a ser criado no ano de 2014, com atualizaçoes até os dias de hoje')
            point1 = int(input('De acordo com as informações digite uma nota de 0 a 100'))
            print(point1)
        elif analisar == '2':
            print('não é apresentado quanto foi gasto na criação do jogo ')
            point2 = int(input('De acordo com as informações digite uma nota de 0 a 100'))
            print(point2)
        elif analisar == '3':
            print('o criador foi Evan Debenham, não temos informaçoes de outros membros da equipe atualmente, porém é um jogo indie de grupo pequeno, vindo da empresa Shattered Pixel Games ')
            point3 = int('De acordo com as informações digite uma nota de 0 a 100')
            print(point3)
        elif analisar == '4':
            print('Shattered Pixel Dungeon é um roguelike 2D com mecânicas de dungeon crawler. O jogo é uma versão expandida e melhorada do clássico Pixel Dungeon, com gráficos pixelados e combate baseado em turnos. Nele, você explora masmorras geradas aleatoriamente, enfrentando inimigos e coletando itens para fortalecer seu personagem. A história é simples, focando em sobrevivência e exploração, enquanto a cada morte o jogador recomeça com novos desafios. O jogo oferece várias classes de personagens e muitas opções de personalização, garantindo uma experiência única a cada jogada.')
            point4 = int('De acordo com as informações digite uma nota de 0 a 100')
            print(point4)