def menor_numero(lista):
    num = lista[0]
    for i in lista:
        if i < num:
            num = i
    return num


def maior_numero(lista):
    num = lista[0]
    for i in lista:
        if i > num:
            num = i
    return num


def soma_numeros(lista):
    lista.sort()
    numero_menor = lista[0]
    numero_maior = lista[-1]
    soma = numero_menor + numero_maior
    return soma


def soma_todos_numeros(lista):
    soma = 0
    for i in lista:
        soma += i
    return int(soma)


def media_dos_numeros(lista):
    num = len(lista)
    media = soma_todos_numeros(lista) / num
    return media


lista = [1, 5, 33, 8, 77, 43, 124, 6, 8, 99]

menor_num = menor_numero(lista)
print(f"O menor numero da lista e: {menor_num}")
maior_num = maior_numero(lista)
print(f"O maior numero da lista e: {maior_num}")
soma = soma_numeros(lista)
print(f"A soma dos numeros e {soma}")
soma_total = soma_todos_numeros(lista)
print(f"A soma total dos numeros e: {soma_total}")
media_num = media_dos_numeros(lista)
print(f"A media dos numeros da array e: {media_num}")