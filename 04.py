numeros = [12, 342, 345, 2, 8, 7896]
contador = 0  # contador de digitos pares
for numero in numeros:
    # converte o numero para string para ulilizar a funcao len()
    numero_str = str(numero)
    if len(numero_str) % 2 == 0:
        contador += 1  # incrementa o contador se o numero tiver digitos pares
    print(f"O numero {numero_str} tem {contador} digitos pares")
contador = 0  # reseta o contador para a proxima iteracao