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

#COM COMRESSÃO
def achatar(lista):
    return [
        x
        for elemento in lista
        for x in (achatar(elemento) if isinstance(elemento, list) else [elemento])
    ]


lista = [1, 2, [4, 2], 5, [2, [1, 2, 3], [[1]]], 8]

print(achatar(lista))