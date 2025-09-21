def NumUnico(array):  # definicao da funcao
    num = 0  # declarar variavel num  igual a zero
    for i in array:  # for do array
        num ^= i    # compara o bit dos numeros
    return num


array = [1, 2, 2, 1, 3, 3, 4, 5, 5, 6, 6]
unico = NumUnico(array)
print(unico)