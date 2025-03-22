with open('hero.txt', 'w', encoding='utf-8') as mensagem:
       mensagem.write('Spide-man , Marvel')

with open('hero.txt', 'w', encoding='utf-8') as arquivo:
       conteudo = arquivo.read()
       print(conteudo)