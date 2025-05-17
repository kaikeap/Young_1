class Livro():
    def __init__(self,titulo,autor,pagina):
        self.titulo = input('digite o titulo: ')
        self.autor = input('digite o autor: ')
        self.pagina = input('digite quantas paginas: ')

    def detalhes(self):
        return f'titulo: {self.titulo} \nautor: {self.autor} \npagina: {self.pagina}'
    
Livro1 = Livro('','','')
print(Livro1.detalhes())