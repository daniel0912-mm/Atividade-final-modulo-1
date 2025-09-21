meu_array = [1, 2, 3, 2, 1, 4, 10]
dicionario = {}
for numero in meu_array:
    if numero in dicionario:
        dicionario[numero] += 1
    else:
        dicionario[numero] = 1

print(dicionario)