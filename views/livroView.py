from controllers.livro import *


def viewLivro():
    opcao = int(input("[1]Novo Livro [2]Atualizar Livro [3]Excluir Livro [4]Vizualizar Livros\n=>"))

    if opcao == 1:
        print("store")

    elif opcao == 2:
        print("Update")

    elif opcao == 3:
        print("Excluir")

    elif opcao == 4:
        exibirlivros()
