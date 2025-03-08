from datetime import datetime

agora = datetime.now()
proximo_ano = datetime(datetime.now().year + 1, 1, 1)
dias_restantes = (proximo_ano - agora). days
print(dias_restantes)