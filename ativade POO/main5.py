class Aluno():
    def __init__ (self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
    
    def media(self):
        return f'ÓLa {self.nome} você teve media: {(self.nota1 + self.nota2) / 2}'
    
    def status(self):
        if((self.nota1 + self.nota2) / 2) > 6:
            return 'Aprovado'
        else:
            return 'Reprovado'

Aluno1 = Aluno('Kaike Ap.',10,10)
print(Aluno1.media())
print(Aluno1.status())
