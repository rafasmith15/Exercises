class Contato:
    def __init__(self, nome, telefone, email, favorito=False) -> None:
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.favorito = favorito

class Agenda:
    def __init__(self) -> None:
        self.contatos = []

    def add_contato(self, contato):
        self.contatos.append(contato)   

    def listar_contatos(self):
        for contato in self.contatos:
            print(f"Nome:{contato.nome}, Telefone:{contato.telefone}, Email:{contato.email},Favorito: {'Sim' if contato.favorito else 'Não'}")  