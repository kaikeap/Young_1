class AgendaDeContatos:
    def __init__(self, MyListCon):
            self.MyListCon = []
            self.MyListCon = MyListCon
    def AdicionarContato(self):
        NvCon = input('Qual contato deseja adicionar?: ')
        self.MyListCon.append(NvCon)
    def RemoverContatos(self):
        RemovCon = input('qual contato deseja remover?: ')
        if RemovCon in self.MyListCon:
            self.MyListCon.remove(RemovCon)
            print(f'Contato {RemovCon} removido com secesso')
        else:
            print(f'Contato {RemovCon} não encontrado')
    def MostrarContatos(self):
        print("Contatos na agenda:")
        for contato in self.MyListCon:
            print(contato)
agenda = AgendaDeContatos(['Andrew', 'PROF', 'Julho'])
agenda.MostrarContatos()
agenda.AdicionarContato()
agenda.MostrarContatos()
agenda.RemoverContatos()
agenda.MostrarContatos()