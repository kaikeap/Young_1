import main as pc

nome_maquina = 'Maria'
pc.saudacoes(nome_maquina)
while True:
    texto = pc.recebeTexto()
    resposta = pc.BuscarTexto(nome_maquina, texto)
    if pc.exibirResposta(resposta, nome_maquina) == 'fim':
        break