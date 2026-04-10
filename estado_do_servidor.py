servidor = {"status": "ok", "tempo_resposta": 350}

match servidor["status"]:
    case "ok" if servidor["tempo_resposta"] > 200:
        print("Servidor lento")
    case "ok":
        print("Servidor ativo")
    case "erro":
        print("Servidor indisponível")
    case _:
        print("Estado desconhecido")
