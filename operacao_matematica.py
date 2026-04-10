op = input("Operação: ")
n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))

match op:
    case "soma":
        print(n1 + n2)
    case "subtrai":
        print(n1 - n2)
    case "multiplica":
        print(n1 * n2)
    case "divide":
        print(n1 / n2)
    case _:
        print("Operação inválida")
