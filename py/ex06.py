texto = input("Digite uma frase: ")

vogais = "aeiouAEIOU"

quantidade = sum(1 for letra in texto if letra in vogais)

print(quantidade)