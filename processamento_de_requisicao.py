req = {"metodo": "POST", "conteudo": ""}

match req["metodo"]:
    case "GET":
        print("Requisição GET recebida")
    case "POST" if req["conteudo"]:
        print("Requisição POST com dados válidos")
    case "POST":
        print("Requisição POST sem dados")
    case _:
        print("Método não suportado")
