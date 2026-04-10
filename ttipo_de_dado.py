valor = [10, 20, 30]

match valor:
    case int():
        print("Número inteiro")
    case float():
        print("Número decimal")
    case list():
        print("Lista")
    case str() if valor.isnumeric():
        print("String numérica")
    case str():
        print("String textual")
    case _:
        print("Tipo desconhecido")
