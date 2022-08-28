from random import randrange

escolha = 0
numeroMenu = 1


def escolhaDado():
    escolha = int(input("Qual o numero de lados do dado que deseja?(4, 6, 8,  10, 12 ou 20 lados)\n"))

    if escolha == 4:
        d4 = str(randrange(1, 5))
        print("O dado deu o seguinte número: " + d4 + "\n")
    if escolha == 6:
        d6 = str(randrange(1, 7))
        print("O dado deu o seguinte número: " + d6 + "\n")
    if escolha == 8:
        d8 = str(randrange(1, 9))
        print("O dado deu o seguinte número: " + d8 + "\n")
    if escolha == 10:
        d10 = str(randrange(1, 11))
        print("O dado deu o seguinte número: " + d10 + "\n")
    if escolha == 12:
        d12 = str(randrange(1, 13))
        print("O dado deu o seguinte número: " + d12 + "\n")
    if escolha == 20:
        d20 = str(randrange(1, 21))
        print("O dado deu o seguinte número: " + d20 + "\n")


while numeroMenu != 0 :
        numeroMenu = int(input("Deseja jogar o dado? (1 para SIM 0 para não)"))
        if numeroMenu == 1:
            escolhaDado()

