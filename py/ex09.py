n = int(input("Digite n: "))

primos = []

for numero in range(2, n + 1):
    primo = True

    for divisor in range(2, numero):
        if numero % divisor == 0:
            primo = False
            break

    if primo:
        primos.append(numero)

print(primos)