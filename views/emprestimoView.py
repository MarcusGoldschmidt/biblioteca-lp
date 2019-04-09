from controllers.emprestimos import *

def viewEmprestimo():
    opcao = int(input("[1]Emprestimo de livro [2]Devolver Livro \n=> "))

    if opcao == 1:
        store()
    elif opcao == 2:
        devolveEmprestimo()
