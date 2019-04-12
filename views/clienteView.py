from controllers.cliente import *


def viewCliente():
    opcao = int(input("[1]Novo Cliente [2]Atualizar Cliente [3]Excluir Cliente [4]Vizualizar Clientes [5]Sair \n=>"))

    if opcao == 1:
        store()
    elif opcao == 2:
        update()
    elif opcao == 3:
        delete()
    elif opcao == 4:
        exibirclientes()
