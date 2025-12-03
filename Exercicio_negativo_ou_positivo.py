numero = int(input("Digite um número: "))

match numero:
    case n if n < 0:
        print("Negativo")

    case 0:
        print("Zero")

    case n if n > 0:
        # positivo → verificar categorias específicas
        if n % 3 == 0 and n % 5 == 0:
            print("Divisível por 3 e 5")
        elif n % 2 != 0:
            print("Positivo e ímpar")
        elif n % 2 == 0:
            print("Positivo e par")
        else:
            print("Outro número positivo")
