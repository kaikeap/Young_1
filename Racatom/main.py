
def game1():
    nota = []
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
            point1 = int(input('De acordo com as informações digite uma nota de 0 a 100\n'))
            nota.append(point1)    
        elif analisar == '2':
            print('não revelada atualmente, porém é um jogo indie de grupo pequeno, vindo da empresa Acid nerve que também fezo jogo Titan souls(2015)')
            point2 = int(input('De acordo com as informações digite uma nota de 0 a 100\n'))
            nota.append(point2) 
        elif analisar == '3':
            print('Infelizmente não foram reveladas as pessoas por trás da criação com exceção do criador da Acid narver Mark Foster e o cofundador David Fenn')
            point3 = int(input('De acordo com as informações digite uma nota de 0 a 100\n'))
            nota.append(point3)   
        elif analisar == '4':
            print("Death's Door é um action-adventure 2D com arte desenhada à mão, criando um mundo vibrante e melancólico." 
            " O jogo foca em combate rápido, onde você controla um ceifador que deve recuperar sua alma roubada, enfrentando chefes e resolvendo puzzles." 
            " A história explora temas de vida e morte, enquanto você coleta almas e melhora suas habilidades."
            " O jogo combina exploração, magias e uma narrativa envolvente, com uma mecânica de combate fluida e dinâmica")
            point4 = int(input('De acordo com as informações digite uma nota de 0 a 100\n'))
            nota.append(point4)  
        elif analisar == '5':
            print("​Death's Door possui uma avaliação de 8.1 no Metacritic, baseada em 471 avaliações de usuários")
            print("algumas notas de usuarios")
            print('"Nota 10: "Eu amo este jogo. A quantidade de história é suficiente para torná-lo intrigante, mas sem sobrecarregar com diálogos intermináveis. Os inimigos e chefes são desafiadores, mas não excessivamente difíceis. A música é excelente." — NikkJagger"')
            print('Nota 6: "O game brinca bastante com perspectivas de forma simples e funciona muito bem." — Raphael Batista, em sua análise para o MeuPlayStation ')
            print('Nota 3: "O jogo é muito bonito, mas a falta de um mapa e a exploração exaustiva me deixaram perdido várias vezes." — Comentário de usuário no Metacritic')
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

##def game1():
##    nota = []
##    etapas_completas = [False] * 5  # Lista para verificar se as 5 etapas foram completadas
##    while True:
##        print("Death's door")
##        print('_______________________________________________')
##        print('===== (1) tempo gasto e ano de criação=========')
##        print('===== (2) dinheiro gasto=======================')
##        print('===== (3) pessoas da equipe====================')
##        print('===== (4) arte,historia e gameplay=============')
##        print('===== (5) metacritic e opnião de jogadores=====')
##        print('===== (6) analise final========================')
##        print('_______________________________________________')
##
##        # Verifica se ao menos uma etapa foi completada
##        if any(etapas_completas):
##            analisar = input('O que pretende analizar ? (Opção 6 disponível após completar pelo menos uma análise)\n')
##        else:
##            analisar = input('O que pretende analizar ? (Opção 6 somente depois de completar pelo menos uma análise)\n')
##
##        if analisar == '1':
##            print('O jogo começou a ser criado no de 2019, tendo um tempo de criação de cerca de 2 anos, sendo lançado em 2021')
##            point1 = int(input('De acordo com as informações digite uma nota de 0 a 100\n'))
##            nota.append(point1)
##            etapas_completas[0] = True  # Marca que a etapa 1 foi completada
##
##        elif analisar == '2':
##            print('não revelada atualmente, porém é um jogo indie de grupo pequeno, vindo da empresa Acid nerve que também fez jogo Titan Souls(2015)')
##            point2 = int(input('De acordo com as informações digite uma nota de 0 a 100\n'))
##            nota.append(point2)
##            etapas_completas[1] = True  # Marca que a etapa 2 foi completada
##
##        elif analisar == '3':
##            print('Infelizmente não foram reveladas as pessoas por trás da criação com exceção do criador da Acid Nerve Mark Foster e o cofundador David Fenn')
##            point3 = int(input('De acordo com as informações digite uma nota de 0 a 100\n'))
##            nota.append(point3)
##            etapas_completas[2] = True  # Marca que a etapa 3 foi completada
##
##        elif analisar == '4':
##            print("Death's Door é um action-adventure 2D com arte desenhada à mão, criando um mundo vibrante e melancólico." 
##                  " O jogo foca em combate rápido, onde você controla um ceifador que deve recuperar sua alma roubada, enfrentando chefes e resolvendo puzzles." 
##                  " A história explora temas de vida e morte, enquanto você coleta almas e melhora suas habilidades."
##                  " O jogo combina exploração, magias e uma narrativa envolvente, com uma mecânica de combate fluida e dinâmica")
##            point4 = int(input('De acordo com as informações digite uma nota de 0 a 100\n'))
##            nota.append(point4)
##            etapas_completas[3] = True  # Marca que a etapa 4 foi completada
##
##        elif analisar == '5':
##            print("Death's Door possui uma avaliação de 8.1 no Metacritic, baseada em 471 avaliações de usuários")
##            print("Algumas notas de usuários:")
##            print('"Nota 10: "Eu amo este jogo... — NikkJagger"')
##            print('Nota 6: "O game brinca com perspectivas... — Raphael Batista"')
##            print('Nota 3: "O jogo é muito bonito... — Comentário de usuário no Metacritic"')
##            point5 = int(input('De acordo com as informações digite uma nota de 0 a 100\n'))
##            nota.append(point5)
##            etapas_completas[4] = True  # Marca que a etapa 5 foi completada
##
##        elif analisar == '6':
##            if not any(etapas_completas):  # Se nenhuma etapa foi completada, bloqueia a opção 6
##                print("Você precisa fazer pelo menos uma análise antes de ver a análise final!")
##                continue  # Volta para o início do loop
##            soma = sum(nota)
##            quantidade = len(nota)
##            total = int(soma / quantidade)
##            print(f'A sua nota final para esse jogo foi {total}')
##            break  # Sai do loop após a análise final