def permicaoFile(type):
    if type == 1:
        return "r"
    elif type == 2:
        return "w"
    elif type == 3:
        return "a"
    else:
        print("Permição não existe")
        return ""


def abrirarquivo(arquivo, permisao):
    try:
        file = open("database/" + str(arquivo), permicaoFile(permisao))
    except OSError as err:
        print("Falha na abertura do Arquivo")
        return 0
    else:
        return file


def escrevefile(data, arquivo):
    file = abrirarquivo(arquivo, 2)

    if file == 0:
        return 0

    for row in data:
        for column in row:
            if column == row[-1]:
                file.write(column)
            else:
                file.write(str(column) + ',')
    file.close()
    return 1


def escrevefilefinal(data, arquivo):
    file = abrirarquivo(arquivo, 3)

    if file == 0:
        return 0

    file.write('\n')

    for column in data:
        if column == data[-1]:
            file.write(column)
        else:
            file.write(str(column) + ',')
    file.close()
    return 1


def lerarquivo(arquivo):
    file = abrirarquivo(arquivo, 1)
    if file == 0:
        return 0
    return [x.split(',') for x in file]
