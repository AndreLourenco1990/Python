pedido = {"tipo": "venda", "valor": 250}

match pedido["tipo"]:
    case "compra":
        print(f"Compra de {pedido['valor']}€")
    case "venda":
        print(f"Venda de {pedido['valor']}€")
    case _:
        print("Pedido desconhecido")
