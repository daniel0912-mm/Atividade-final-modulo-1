lista = [1,3,5,6,7]
lista_2 = []
for i in lista: 
    lista_2.append(i*2)
print(f'lista_2: {lista_2}')

dicionario = dict(zip(lista, lista_2))
print(f'Dicionario: {dicionario}')