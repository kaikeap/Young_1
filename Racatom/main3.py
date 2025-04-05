def game3():
    while True:
        print("rucoy online")
        print('_______________________________________')
        print('===== (1) tempo gasto e ano de criação=')
        print('===== (2) dinheiro gasto===============')
        print('===== (3) pessoas da equipe============')
        print('===== (4) arte,historia e gameplay=====')
        print('_______________________________________')
        analisar = input('O que pretende analizar ?\n')
        if analisar == '1':
            print('O jogo começou a ser desenvolvido em janeiro de 2016, com atualizaçoes até os dias de hoje')
            point1 = int(input('De acordo com as informações digite uma nota de 0 a 100'))
            print(point1)
        elif analisar == '2':
            print('não é apresentado quanto foi gasto na criação do jogo ')
            point2 = int(input('De acordo com as informações digite uma nota de 0 a 100'))
            print(point2)
        elif analisar == '3':
            print('o criador foi Ricardo Gonzales, não temos informaçoes de outros membros da equipe atualmente, porém é um jogo indie de grupo pequeno, vindo da empresa fundou a Acid Studios ')
            point3 = int('De acordo com as informações digite uma nota de 0 a 100')
            print(point3)
        elif analisar == '4':
            print('Rucoy Online é um MMORPG 2D em mundo aberto, com foco em exploração, combate e progressão de personagem. O jogo possui uma estética simples e visual em pixel art. Nele, você cria um personagem e escolhe entre diferentes classes (como guerreiro, mago ou arqueiro), enfrentando monstros e completando missões. A história do jogo é mais voltada para a exploração, com o objetivo principal sendo o aumento de nível e conquista de novos equipamentos. Rucoy Online é totalmente gratuito e oferece um modo multijogador dinâmico, permitindo interações entre jogadores, como batalhas e comércio.')
            point4 = int('De acordo com as informações digite uma nota de 0 a 100')