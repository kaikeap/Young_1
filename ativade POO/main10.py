class AgendaDeContatos:
    def __init__(self, MyListCon):
            self.MyListCon = []
            self.MyListCon = MyListCon

    def AdicionarContato(self):
        NvCon = input('Qual contato deseja adicionar?: ')
        self.MyListCon.append(NvCon)

    def MostrarContatos(self):
        print("Contatos na agenda:")
        for contato in self.MyListCon:
            print(contato)

agenda = AgendaDeContatos(['Andrew', 'PROF', 'Julho'])
agenda.MostrarContatos()
agenda.AdicionarContato()
agenda.MostrarContatos()
