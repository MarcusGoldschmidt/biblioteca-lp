from controllers.emprestimos import *


def viewEmprestimo():
    opcao = int(input(
        "[1]Emprestimo de livro [2]Devolver Livro [3]Renovar Emprestimo [4]Lista livros emprestados do usuario\n=> "))

    if opcao == 1:
        store()
    elif opcao == 2:
        devolveEmprestimo()
    elif opcao == 3:
        renovaremprestimo()
    elif opcao == 4:
        listalivrosemprestadosusuario()
    else:
        print("Opção inválida")
