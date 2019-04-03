from controllers.cliente import exibirclientes
from controllers.fileMethods import *
from controllers.livro import exibirlivros
import datetime

DB_EMPRESTIMOS = "Emprestimos.csv"


def index():
    return lerarquivo(DB_EMPRESTIMOS)


def store():
    emprestimo = []

    exibirclientes()
    cpf = str(input("CPF => "))

    exibirlivros()
    livro = str(input("ID Livro"))

    emprestimo.append(numeroregistros(DB_EMPRESTIMOS) + 1)
    emprestimo.append(livro)
    emprestimo.append(cpf)
    emprestimo.append(str(datetime.datetime.now().strftime("%d/%m/%Y")))

    # Maximo da entrega
    data = input("Data **/**/**** => ").split('/')
    map(lambda x: int(x), data)
    emprestimo.append(datetime.datetime(data[2], data[1], data[0]).strftime("%d/%m/%Y"))

    # Data da devolução
    data = input("Data **/**/**** => ").split('/')
    map(lambda x: int(x), data)
    emprestimo.append(datetime.datetime(data[2], data[1], data[0]).strftime("%d/%m/%Y"))

    emprestimo.append(0)

    if escrevefilefinal(emprestimo, DB_EMPRESTIMOS):
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
    escrevefile(data, DB_EMPRESTIMOS)


def updateone(newData):
    update = []

    for aux in index():
        if aux[0] == newData[0]:
            aux = newData
        update.append(aux)
    escrevefile(update, DB_EMPRESTIMOS)


def delete(id):
    data = index()
    newData = []

    exibirclientes()

    id = input("Deletar por CPF: ")

    for user in data:
        if user[0] != id:
            newData.append(user)
    escrevefile(newData, DB_EMPRESTIMOS)


def show(id):
    for livro in index():
        if livro[0] == id:
            return livro
    return 0


def exibiremprestimos():
    data = index()

    for i in data:
        for j in i:
            if j == i[-1]:
                print(j)
                break
            print(j + "   |   ", end='')
