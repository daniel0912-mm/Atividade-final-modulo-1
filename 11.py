array = [0, 2, 3, 4, 5, 6, 7, 8]
array2 = []
total = len(array) + 1
num_inicial = array[0]

for i in range(num_inicial, total):
    array2.append(i)

set_array = set(array)
set_array2 = set(array2)

numero_fantando = set_array2 - set_array

print(f"O numero que falta e: {numero_fantando}")