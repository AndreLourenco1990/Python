import os
OPC = 0
saida = True

while saida:
    os.system('cls')
    print("1 - para receber um bom dia")
    print("2 - para receber um boa tarde")
    print("3 - para receber um boa noite")
    print("4 - Sair")
    OPC = int(input("Intruduza a opção: "))

    match OPC:
        case 1:
            print("Bom dia!")
        case 2:
            print("Boa tarde!")
        case 3:
            print("Boa noite!")
        case 4:
            print("Adeus!") 
            break
    