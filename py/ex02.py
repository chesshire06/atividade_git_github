def descendentes(arvore):
    nome, filhos = arvore
    return [filho[0] for filho in filhos] + [
        descendente
        for filho in filhos
        for descendente in descendentes(filho)
    ]


arvore = (
    "João",
    [
        ("Maria", [("Ana", [])]),
        ("Pedro", [])
    ]
)

print(descendentes(arvore))