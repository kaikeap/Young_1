def saudacoes(nome):
    import random
    frases = ['Bom dia! Meu nome é' +nome+ '.Como vai você?','Ola','oi, tudo?']
    print(frases[random.randint(0,2)])

def recebeTexto():
    texto = 'Cliente' +input('Cliente: ')
    palavraProibido = {'Bocó'}
    for p in texto:
        print('Não vem não! Me respeita')
        return(recebeTexto)
    return texto
