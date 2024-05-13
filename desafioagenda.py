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
            print(f"Nome:{contato.nome}, Telefone:{contato.telefone}, Email:{contato.email}, Favorito: {'Sim' if contato.favorito else 'Não'}") 

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

agenda = Agenda()  

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        email = input("Email: ")
        novo_contato = Contato(nome, telefone, email)
        agenda.add_contato(novo_contato)

    elif opcao == "2":
        print("Lista de Contatos:")
        agenda.listar_contatos()

    elif opcao == "3":
        nome = input("Digite o nome do contato que deseja editar: ")
        novo_telefone = input("Novo telefone: ")
        novo_email = input("Novo email: ")
        agenda.editar_contato(nome, novo_telefone, novo_email)

    elif opcao == "4":
        nome = input("Digite o nome do contato: ")
        opcao_favorito = input("Marcar (M) ou Desmarcar (D) como favorito: ").upper()
        if opcao_favorito == "M":
            agenda.marcar_favorito(nome)
        elif opcao_favorito == "D":
            agenda.desmarcar_favorito(nome)
        else:
            print("Opção inválida.")

    elif opcao == "5":
        print("Lista de Contatos Favoritos:")
        agenda.listar_favoritos()

    elif opcao == "6":
        nome = input("Digite o nome do contato que deseja apagar: ")
        agenda.apagar_contato(nome)

    elif opcao == "7":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")    