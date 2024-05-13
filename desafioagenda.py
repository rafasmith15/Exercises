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

    def editar_contato(self, nome, novo_telefone, novo_email):
        for contato in self.contatos:
            if contato.nome == nome:
                contato.telefone = novo_telefone
                contato.email = novo_email
                print("Contato editado com sucesso.")
                return
        print("Contato não encontrado.")  

    def marcar_favorito(self, nome):
        for contato in self.contatos:
            if contato.nome == nome:
                contato.favorito = True
                print("Contato marcado como favorito.")
                return
        print("Contato não encontrado.")     


    def desmarcar_favorito(self, nome):
        for contato in self.contatos:
            if contato.nome == nome:
                contato.favorito = False
                print("Contato desmarcado como favorito.")
                return
        print("Contato não encontrado.")

    def listar_favoritos(self):
        favoritos = [contato for contato in self.contatos if contato.favorito]
        if favoritos:
            print("Lista de contatos favoritos:")
            for contato in favoritos:
                print(f"Nome: {contato.nome}, Telefone: {contato.telefone}, Email: {contato.email}")
        else:
            print("Nenhum contato favorito encontrado.")

    def apagar_contato(self, nome):
        for contato in self.contatos:
            if contato.nome == nome:
                self.contatos.remove(contato)
                print("Contato apagado com sucesso.") 
                return
        print("Contato não encontrado.")


    def menu():
     print("=== Menu ===")
     print("1. Adicionar Contato")
     print("2. Listar Contatos")
     print("3. Editar Contato")
     print("4. Marcar/Demarcar como Favorito")
     print("5. Listar Contatos Favoritos")
     print("6. Apagar Contato")
     print("7. Sair")    