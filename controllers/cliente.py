from controllers.fileMethods import *

DB_CLIENTE = "Usuarios.csv"


def index():
    return lerarquivo(DB_CLIENTE)


def store():
    user = []

    user.append(input("CPF =>"))
    user.append(input("NOME =>"))
    while True:
        user.append(input("TIPO [0]Prof. [1]Estudante =>"))
        if user[2] in ['0', '1']:
            user[2] = "Professor" if user[2] == 0 else "Estudante"
            break
        else:
            print("Valor não permitido!")
    user.append(0)
    user.append("null")

    if escrevefilefinal(user, DB_CLIENTE):
        print("Salvo com sucesso!")
    else:
        print("Erro ao salvar!")

def update():
    data = index()

    exibirclientes()

    id = input("Alterar por CPF: ")

    for user in data:
        if user[0] == id:
            user[0] = input("CPF =>")
            user[1] = input("NOME =>")
            while True:
                user[2] = input("TIPO =>")
                if user[2] in ['0', '1']:
                    user[2] = "Professor" if user[2] == 0 else "Estudante"
                    break
                else:
                    print("Valor não permitido!")
            break
    escrevefile(data, DB_CLIENTE)


def updateonecliente(newData):
    update = []

    for aux in index():
        if aux[0] == newData[0]:
            aux = newData
        update.append(aux)
    escrevefile(update, DB_CLIENTE)


def showCliente(id):
    for data in index():
        if data[0] == id:
            return data
    return 0


def delete():
    data = index()
    newData = []

    exibirclientes()

    id = input("Deletar por CPF: ")

    for user in data:
        if user[0] != id:
            newData.append(user)
    escrevefile(newData, DB_CLIENTE)


def exibirclientes():
    data = index()

    for i in data:
        for j in i:
            if j == i[-1]:
                print(j)
                break
            print(j + "   |   ", end='')


def buscaCliente():
    aux = input("CPF: ")
    cliente = index()
    for i in cliente:
        if cliente[i][0] == aux:
            print(cliente[i][j] for j in i)
            return True

    return False
