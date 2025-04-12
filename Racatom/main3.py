def game3():
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
            print('O jogo começou a ser desenvolvido em janeiro de 2016, com atualizaçoes até os dias de hoje')
            point1 = int(input('De acordo com as informações digite uma nota de 0 a 100\n'))
            nota.append(point1)
        elif analisar == '2':
            print('não é apresentado quanto foi gasto na criação do jogo ')
            point2 = int(input('De acordo com as informações digite uma nota de 0 a 100\n'))
            nota.append(point2)
        elif analisar == '3':
            print('o criador foi Ricardo Gonzales, não temos informaçoes de outros membros da equipe atualmente, porém é um jogo indie de grupo pequeno, vindo da empresa fundou a Acid Studios ')
            point3 = int(input('De acordo com as informações digite uma nota de 0 a 100\n'))
            nota.append(point3)
        elif analisar == '4':
            print('Rucoy Online é um MMORPG 2D em mundo aberto, com foco em exploração, combate e progressão de personagem. O jogo possui uma estética simples e visual em pixel art. Nele, você cria um personagem e escolhe entre diferentes classes (como guerreiro, mago ou arqueiro), enfrentando monstros e completando missões. A história do jogo é mais voltada para a exploração, com o objetivo principal sendo o aumento de nível e conquista de novos equipamentos. Rucoy Online é totalmente gratuito e oferece um modo multijogador dinâmico, permitindo interações entre jogadores, como batalhas e comércio.')
            point4 = int(input('De acordo com as informações digite uma nota de 0 a 100\n'))
            nota.append(point4)
        elif analisar == '5':
            print("rucoy online não possui uma avaliação no Metacritic")
            print("algumas notas de usuarios")
            print('"Nota 10: "Um dos meus MMORPGs favoritos. É o melhor jogo com o menor tamanho. Precisa de um mapa maior e alguns eventos. É um ótimo jogo na minha opinião." — vinda de TapTap"')
            print('Nota 6: "Jogo simples 2D MMO, 3 classes que você pode escolher a qualquer momento no mesmo personagem, também há comércio no jogo." —  análise vindo de GameFAQs ')
            print('Nota 3: "Na minha opinião, tem muitas coisas para melhorar ou adicionar no jogo: Pets, recompensas, desafios que todo mundo possa jogar, facilitar o modo de treino (porque, sinceramente, demora demais para upar), colocar novas armas, armaduras e objetos, criar algum modo de ganhar diamantes sem necessitar gastar dinheiro, etc..." — Comentário de usuário do GooglePlay')
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
