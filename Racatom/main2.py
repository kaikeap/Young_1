def game2():
    nota = []
    while True:
        print("rucoy online")
        print('________________________________________________')
        print('===== (1) tempo gasto e ano de criação==========')
        print('===== (2) dinheiro gasto========================')
        print('===== (3) pessoas da equipe=====================')
        print('===== (4) arte,historia e gameplay==============')
        print('===== (5) Metacritic e opniao dos jodagores=====')
        print('===== (6) analize final ========================')
        print('________________________________________________')
        analisar = input('O que pretende analizar ?\n')
        if analisar == '1':
            print('O jogo começou a ser criado no ano de 2014, com atualizaçoes até os dias de hoje')
            point1 = int(input('De acordo com as informações digite uma nota de 0 a 100\n'))
            nota.append(point1)
        elif analisar == '2':
            print('não é apresentado quanto foi gasto na criação do jogo\n')
            point2 = int(input('De acordo com as informações digite uma nota de 0 a 100\n'))
            nota.append(point2)
        elif analisar == '3':
            print('o criador foi Evan Debenham, não temos informaçoes de outros membros da equipe atualmente, porém é um jogo indie de grupo pequeno, vindo da empresa Shattered Pixel Games ')
            point3 = int(input('De acordo com as informações digite uma nota de 0 a 100\n'))
            nota.append(point3)
        elif analisar == '4':
            print('Shattered Pixel Dungeon é um roguelike 2D com mecânicas de dungeon crawler. O jogo é uma versão expandida e melhorada do clássico Pixel Dungeon, com gráficos pixelados e combate baseado em turnos. Nele, você explora masmorras geradas aleatoriamente, enfrentando inimigos e coletando itens para fortalecer seu personagem. A história é simples, focando em sobrevivência e exploração, enquanto a cada morte o jogador recomeça com novos desafios. O jogo oferece várias classes de personagens e muitas opções de personalização, garantindo uma experiência única a cada jogada.')
            point4 = int(input('De acordo com as informações digite uma nota de 0 a 100\n'))
            nota.append(point4)
        elif analisar == '5':
            print("Shaterred Pixel Dungeon possui uma avaliação de 7.4 no Metacritic, baseada em 8 avaliações de usuários")
            print("algumas notas de usuarios")
            print('"Nota 10: "SPD é um jogo, tanto sua história quanto sua habilidade e originalidade na hora de criar personagens, habilidades ou poderes." — Gerrami"')                
            print('Nota 6: "O game é divertido com mecanicas legais mas enjoa rapido." — sigma984, em sua análise da playStory ')
            print('Nota 3: "O jogo é muito dificil com mecanicas chats." — Comentário de usuário no Metacritic')
            point5 = int(input('De acordo com as informações digite uma nota de 0 a 100\n'))
            nota.append(point5)
        elif analisar == '6':
            soma = sum(nota)
            print(soma)
            quantidade = len(nota)
            print(quantidade)
            total = int(soma/quantidade)
            print(f'A sua nota final para esse jogo foi {total}')
            break
