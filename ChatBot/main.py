def saudacoes(nome):
    import random
    frases = [f'Bom dia! Meu nome é {nome}. Como vai você?', 'Olá', 'Oi, tudo bem?']
    print(random.choice(frases))

def recebeTexto():
    texto = 'Cliente: ' + input('Cliente: ')
    palavraProibido = {'Bocó'}
    for palavra in texto.split():
        if palavra in palavraProibido:
            print('Não vem não! Me respeita')
            return recebeTexto()
    return texto

def BuscarTexto(nome, texto):
    with open('BaseDeConhecimento.txt', 'a+') as conhecimento:
        conhecimento.seek(0)
        linhas = conhecimento.readlines()
        
        if texto.replace('Cliente: ', '') == 'Tchau':
            print(nome + ': volte sempre!')
            return 'fim'

        for i in range(len(linhas)):
            if linhas[i].strip() == texto.strip():
                if i + 1 < len(linhas) and 'Chat: ' in linhas[i+1]:
                    return linhas[i+1].strip()

        print('Me desculpe, não sei o que falar')
        conhecimento.write(texto + '\n')
        resposta_user = input('O que esperava\n')
        conhecimento.write('Chat: ' + resposta_user + '\n')
        return 'Humm. . .'

def exibirResposta(resposta, nome):
    if resposta == 'fim':
        return 'fim'
    print(resposta.replace('ChatBot', nome))
    return 'continuar'
