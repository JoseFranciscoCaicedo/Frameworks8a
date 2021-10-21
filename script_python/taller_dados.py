from random import randint

name = input("Ingrese su nombre: ")

position = 0
acum = 0
play = True

while play :
    dado1 = randint(1,6)
    dado2 = randint(1,6)
    print("")
    print("dado1: ", dado1)
    print("dado2: ", dado2, "\n")

    position = dado1 + dado2

    acum += position

    if(dado1 == dado2):
        print("ha sacado su primer numero par")
        while play :
            dado1 = randint(1,6)
            dado2 = randint(1,6)

            print("dado1: ", dado1)
            print("dado2: ", dado2,"\n")

            position = dado1 + dado2

            acum += position

            if(dado1 == dado2):
                play = False
                print("ha sacado su segundo numero par, el juego ha terminado")

print("El jugador ", name, "Tuvo un acumulado total de: ", acum)