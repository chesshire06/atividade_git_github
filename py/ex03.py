def achatar(lista):
    resultado = []

    for elemento in lista:
        if isinstance(elemento, list):
            resultado.extend(achatar(elemento))
        else:
            resultado.append(elemento)

    return resultado


lista = [1, 2, [4, 2], 5, [2, [1, 2, 3], [[1]]], 8]

print(achatar(lista))