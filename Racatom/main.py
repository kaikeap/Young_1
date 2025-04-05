##data science\matematica aplicada

###Shattered Pixel Dungeon é um jogo de RPG roguelike desenvolvido por Evan Debenham. O jogo foi bem recebido pelos jogadores, com uma pontuação média de 7,7 no Metacritic, baseada em 7 avaliações de usuários.
###
###Nota 10: "Shattered Pixel Dungeon é um ótimo jogo, tanto pela sua história quanto pela jogabilidade e originalidade na criação de personagens, habilidades ou poderes."
###
###Nota 6: "Um roguelike tradicional bem projetado, com toques modernos suficientes para torná-lo acessível a jogadores não tão experientes. Eu particularmente gostei da seleção de classes, pois cada classe tem mecânicas únicas que oferecem um estilo de jogo verdadeiramente diferente das outras."
###
###Nota 3: "Não consigo vencer esse maldito jogo. Meu Deus. Você morre tão facilmente por causa de momentos completamente aleatórios. Claro, esse é meio que o ponto.

def game1():
    while True:
        print("Death's door")
        print('_______________________________________________')
        print('===== (1) tempo gasto e ano de criação=========')
        print('===== (2) dinheiro gasto=======================')
        print('===== (3) pessoas da equipe====================')
        print('===== (4) arte,historia e gameplay=============')
        print('===== (5) metacritic e opnião de jogadores=====')
        print('===== (6) analise final========================')
        print('_______________________________________________')
        analisar = input('O que pretende analizar ?\n')
        if analisar == '1':
            print('O jogo começou a ser criado no de 2019, tendo um tempo de criação de cerca de 2 anos, sendo lançado em 2021')
            point1 = int(input('De acordo com as informações digite uma nota de 0 a 100'))
            print(point1)
            terminar = input('Terminar sua analise? (s/n)')
        elif analisar == '2':
            print('não revelada atualmente, porém é um jogo indie de grupo pequeno, vindo da empresa Acid nerve que também fezo jogo Titan souls(2015)')
            point2 = int(input('De acordo com as informações digite uma nota de 0 a 100'))
            print(point2)
            terminar = input('Terminar sua analise? (s/n)')
        elif analisar == '3':
            print('Infelizmente não foram reveladas as pessoas por trás da criação com exceção do criador da Acid narver Mark Foster e o cofundador David Fenn')
            point3 = int(input('De acordo com as informações digite uma nota de 0 a 100'))
            print(point3)
            terminar = input('Terminar sua analise? (s/n)')
        elif analisar == '4':
            print("Death's Door é um action-adventure 2D com arte desenhada à mão, criando um mundo vibrante e melancólico." 
            " O jogo foca em combate rápido, onde você controla um ceifador que deve recuperar sua alma roubada, enfrentando chefes e resolvendo puzzles." 
            " A história explora temas de vida e morte, enquanto você coleta almas e melhora suas habilidades."
            " O jogo combina exploração, magias e uma narrativa envolvente, com uma mecânica de combate fluida e dinâmica")
            point4 = int(input('De acordo com as informações digite uma nota de 0 a 100'))
            print(point4)
            terminar = input('Terminar sua analise? (s/n)')
        elif analisar == '5':
            print("​Death's Door possui uma avaliação de 8.1 no Metacritic, baseada em 471 avaliações de usuários")
            print("algumas notas de usuarios")
            print('"Nota 10: "Eu amo este jogo. A quantidade de história é suficiente para torná-lo intrigante, mas sem sobrecarregar com diálogos intermináveis. Os inimigos e chefes são desafiadores, mas não excessivamente difíceis. A música é excelente." — NikkJagger"')
            print('Nota 6: "O game brinca bastante com perspectivas de forma simples e funciona muito bem." — Raphael Batista, em sua análise para o MeuPlayStation ')
            print('Nota 3: "O jogo é muito bonito, mas a falta de um mapa e a exploração exaustiva me deixaram perdido várias vezes." — Comentário de usuário no Metacritic')
            terminar = input('Terminar sua analise? (s/n)')    
