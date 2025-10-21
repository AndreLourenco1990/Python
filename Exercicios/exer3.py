import random

# opções possíveis
opcoes = ["pedra", "papel", "tesoura"]

print("=== Pedra, Papel ou Tesoura ===")
print("1 - Jogar contra o computador")
print("2 - Jogar entre dois jogadores")

modo = input("Escolhe o modo (1 ou 2): ")


if modo == "1":
    jogador = input("Escolhe pedra, papel ou tesoura: ").lower()
    computador = random.choice(opcoes)

    print(f"\nTu escolheste: {jogador}")
    print(f"O computador escolheu: {computador}\n")

    match (jogador, computador):
        case (a, b) if a == b:
            print("Empate!")
        case ("pedra", "tesoura") | ("papel", "pedra") | ("tesoura", "papel"):
            print("Ganhaste!")
        case ("pedra", "papel") | ("papel", "tesoura") | ("tesoura", "pedra"):
            print("Perdeste!")
        case _:
            print("Escolha inválida.")


elif modo == "2":
    jogador1 = input("Jogador 1, escolhe pedra, papel ou tesoura: ").lower()
    jogador2 = input("Jogador 2, escolhe pedra, papel ou tesoura: ").lower()

    match (jogador1, jogador2):
        case (a, b) if a == b:
            print("Empate!")
        case ("pedra", "tesoura") | ("papel", "pedra") | ("tesoura", "papel"):
            print("Jogador 1 ganhou!")
        case ("pedra", "papel") | ("papel", "tesoura") | ("tesoura", "pedra"):
            print("Jogador 2 ganhou!")
        case _:
            print("Escolha inválida.")

else:
    print("Opção inválida. Escolhe 1 ou 2.")