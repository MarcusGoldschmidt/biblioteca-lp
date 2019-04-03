from controllers.fileMethods import *

DB_LIVRO = "Livros.csv"


def index():
    return lerarquivo(DB_LIVRO)


def store():
    data = []

    data.append(numeroregistros(DB_LIVRO) + 1)
    data.append(input("Título"))
    data.append(input("Autor"))
    data.append(input("Área"))
    data.append(input("Páginas"))
    data.append(input("Ano"))
    data.append(input("Palabra-chave 1"))
    data.append(input("Palabra-chave 2"))
    data.append(input("Palabra-chave 3"))
    data.append(0)

    if escrevefilefinal(data, DB_LIVRO):
        print("Salvo com sucesso!")
    else:
        print("Erro ao salvar!")


def update():
    data = index()

    exibirlivros()

    id = input("Alterar por ID: ")

    for livro in data:
        if livro[0] == id:
            livro[1] = input("CPF =>")
            livro[2] = input("Autor =>")
            livro[3] = input("Área =>")
            livro[4] = input("Autor =>")
            livro[5] = input("Páginas =>")
            livro[6] = input("Palabra-chave 1 =>")
            livro[7] = input("Palabra-chave 2 =>")
            livro[8] = input("Palabra-chave 3 =>")
    escrevefile(data, DB_LIVRO)


def updateonelivro(newData):
    update = []

    for aux in index():
        if aux[0] == newData[0]:
            aux = newData
        update.append(aux)
    escrevefile(update, DB_LIVRO)


def showLivro(id):
    for data in index():
        if data[0] == id:
            return data
    return 0


def exibirlivros():
    data = index()

    for i in data:
        for j in i:
            if j == i[-1]:
                print(j)
                break
            print(j + "   |   ", end='')


def exibirlivro(data):
    for i in data:
        print(i + "   |   ", end='')
    print()
