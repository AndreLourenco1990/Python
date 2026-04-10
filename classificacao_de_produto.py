produto = {"categoria": "eletrônico", "preco": 1500}

match produto["categoria"]:
    case "eletrônico" if produto["preco"] > 1000:
        print("Produto de luxo")
    case "eletrônico":
        print("Produto comum")
    case "alimento":
        print("Produto alimentar")
    case _:
        print("Categoria desconhecida")
