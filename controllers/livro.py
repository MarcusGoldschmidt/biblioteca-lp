from controllers.fileMethods import *

DB_LIVRO = "Livros.csv"


def index():
    return lerarquivo(DB_LIVRO)


def store(data):
    if escrevefile(data, DB_LIVRO, 2):
        print("Salvo com sucesso!")
    else:
        print("Erro ao salvar!")


def exibirlivros():
    data = index()

    for i in data:
        for j in i:
            if j == i[-1]:
                print(j)
                break
            print(j + "   |   ", end='')
