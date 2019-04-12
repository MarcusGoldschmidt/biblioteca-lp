from controllers.livro import *


def viewLivro():
    opcao = int(input("[1]Novo Livro [2]Atualizar Livro [3]Excluir Livro [4]Buscar Livro [5]Vizualizar Livros\n=>"))

    if opcao == 1:
        store()
    elif opcao == 2:
        update()
    elif opcao == 3:
        deletelivro()
    elif opcao == 4:
        buscaLivro()
    elif opcao == 5:
        exibirlivros()
