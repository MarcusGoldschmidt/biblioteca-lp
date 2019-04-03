from controllers.cliente import exibirclientes, showCliente, updateonecliente
from controllers.fileMethods import *
from controllers.livro import exibirlivros, showLivro, updateonelivro, index as indexLivro, exibirlivro
import datetime

DB_EMPRESTIMOS = "Emprestimos.csv"


def index():
    return lerarquivo(DB_EMPRESTIMOS)


def store():
    emprestimo = []

    exibirclientes()
    cpf = str(input("CPF => "))
    cliente = showCliente(cpf)

    if cliente[3] == 3:
        print("Maximo de livros emprestados")
        return 0

    exibirlivros()
    idlivro = str(input("ID Livro"))
    livro = showLivro(idlivro)

    emprestimo.append(numeroregistros(DB_EMPRESTIMOS) + 1)
    emprestimo.append(idlivro)
    emprestimo.append(cpf)
    # Inicio da reserva
    emprestimo.append(str(datetime.datetime.now().strftime("%d/%m/%Y")))

    # Maximo da entrega
    data = str(datetime.datetime.now().strftime("%d/%m/%Y"))
    data = calculoentrega([int(x) for x in data], cliente[2])
    emprestimo.append(data)

    print("Entraga em " + data)

    # Data da devolução
    emprestimo.append("NULL")

    # Quantidade de renovações
    emprestimo.append(0)

    # Atualizar Livro
    livro[9] = 1
    updateonelivro(livro)

    # Atualizar Cliente
    cliente[3] += 1
    updateonecliente(cliente)

    if escrevefilefinal(emprestimo, DB_EMPRESTIMOS):
        print("Salvo com sucesso!")
    else:
        print("Erro ao salvar!")


def calculoentrega(datainicio, tipo):
    if tipo == "Estudante":
        datainicio[2] += 7
    else:
        datainicio[2] += 15

    if datainicio[2] > 30:
        datainicio[2] -= 30
        datainicio[1] += 1
        if datainicio[1] > 12:
            datainicio[1] -= 12
            datainicio[0] += 1

    return datetime.datetime(datainicio[2], datainicio[1], datainicio[0]).strftime("%d/%m/%Y")


def listalivrosemprestadosusuario():
    exibirclientes()
    cpf = str(input("CPF => "))

    dataInicio = [int(x) for x in input("Data inicial **/**/****").split("/")]

    dataFinal = [int(x) for x in input("Data Final **/**/****").split("/")]

    emprestimos = index()
    livros = indexLivro()

    for emprestimo in emprestimos:
        if emprestimo[2] == cpf and comparardata(dataInicio, emprestimo[4]) and comparardata(emprestimo[6], dataFinal):
            for livro in livros:
                if emprestimo[1] == livro[0]:
                    exibirlivro(livro)


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
    for data in index():
        if data[0] == id:
            return data
    return 0


def exibiremprestimos():
    data = index()

    for i in data:
        for j in i:
            if j == i[-1]:
                print(j)
                break
            print(j + "   |   ", end='')


# Verifica se a data é maior
# Recebendo **/**/**** strings
def comparardata(datamenor, datamaior):
    if datamaior[2] > datamenor[2]:
        return True
    elif datamaior[1] > datamenor[1]:
        return True
    elif datamaior[0] > datamenor[0]:
        return True
    else:
        return False
