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


def deletelivro():
    data = index()
    newData = []
    exibirlivros()

    id = input("excluir por ID: ")

    for livro in data:
        if livro[0] != id:
            newData.append(livro)

    escrevefile(newData, DB_LIVRO)


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


def buscaKeyword():
    keyword = input("Palavra-chave: ")
    livros = index()
    flag = False
    for livro in livros:
        if livro[6] == keyword or livro[7] == keyword or livro[8] == keyword:
            exibirlivro(livro)
            flag = True
            return True
    if flag == False:
        print("Palavra chave não encontrada!")
        return False


def buscaTitulo():
    title = input("Título do livro: ")
    livros = index()
    flag = False
    for livro in livros:
        if livro[1] == title:
            exibirlivro(livro)
            flag = True
            return True
    if flag == False:
        print("Título não encontrado!")
        return False


def buscaAutor():
    autor = input("Autor do livro: ")
    livros = index()
    flag = False
    for livro in livros:
        exibirlivro(livro)
        flag = True
    if flag == False:
        print("Autor não encontrado!")
        return False
    else:
        return True  # Ficou no final caso haja mais livros do mesmo autor, para a função não retornar logo o valor e parar de procurar


def buscaArea():
    area = input("Área do livro: ")
    livros = index()
    flag = False
    for livro in livros:
        exibirlivro(livro)
        flag = True
    if flag == False:
        print("Nenhuma publicação da Área foi encontrada!")
        return False
    else:
        return True


def buscaLivro():
    aux = input("Escolha o critério de Busca.\n[1]Keyword\n[2]Título\n[3]autor\n[4]Área\n[5]Sair \n Opção : ")
    if aux == 1:
        buscaKeyword()
    elif aux == 2:
        buscaTitulo()
    elif aux == 3:
        buscaAutor()
    elif aux == 4:
        buscaArea()
    elif aux == 5:
        return 0
    else:
        return buscaLivro()
