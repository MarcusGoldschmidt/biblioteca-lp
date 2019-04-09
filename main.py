from views.clienteView import viewCliente
from views.livroView import viewLivro




while True:

    # TODO: Logica aqui

    opcao = int(input("[1]Livro [2]Cliente [3]Sair\n=>"))

    if opcao == 1:
        viewLivro()
    elif opcao == 2:
        viewCliente()
    elif opcao == 3:

        print("Saindo...")
        break
