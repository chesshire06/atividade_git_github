def lerLista():
    numeros = list(map(int, input("Digite os números separados por espaço: ").split()))
    return numeros


lista = lerLista()
print(lista)