import random

jugando = True 

anch = 80
ast = anch * '*'
print(ast)
print ("\033[1m" + "BIENVENIDO AL JUEGO DE PIEDRA, PAPEL O TIJERA" + "\033[0m")
print ("Instrucciones: Escribe una de las 3 opciones como se indica 'Piedra' 'Papel' 'Tijera'")

while jugando:
    anch = 80
    ast = anch * '*'
    print(ast)
    print("\033[1m" + "Piedra, Papel O Tijera" + "\033[0m")

    pc = random.choice(["Piedra", "Papel","Tijera"])

    player = raw_input("Escriba la opcion que desee: ").capitalize() 


    if player == "Piedra":
        if pc == "Piedra":
            print ("PC elije 'Piedra'. Es un Empate.")
        elif pc == "Papel":
            print ("PC elije 'Papel'. Papel envuelve a Piedra, por lo tanto pierdes :(")
        else:
            print ("PC elige 'Tijera'. Piedra rompe Tijeras, por lo tanto ganas :)")

    elif player == "Papel":
        if pc == "Papel":
            print ("PC elije 'Papel'. Es un Empate.")
        elif pc == "Piedra":
            print ("PC elije 'Piedra'. Papel envuelve a Piedra, por lo tanto ganas :)")
        else:
            print ("PC elige 'Tijera'. Tijeras corta Papel, por lo tanto pierdes :(")

    elif player == "Tijera":
        if pc == "Tijera":
            print ("PC elije 'Tijera'. Es un Empate.")
        elif pc == "Papel":
            print ("PC elije 'Papel'. Tijera corta a Papel, por lo tanto ganas :)")
        else:
            print ("PC elige 'Piedra'. Piedra rompe Tijera, por lo tanto pierdes :(")
    else:
        print ("No has escogido una opcion valida.")

    
    continuar = ""
    while continuar != 'n' or continuar != "s":
        continuar = raw_input("Quieres volver a jugar? (s/n): ")

        if continuar == 'n'.capitalize():
            jugando = False
            print ("\033[1m" + "\nGRACIAS POR JUGAR HASTA LA PROXIMA " + "\033[0m")
            break

        elif continuar == 's'.capitalize():
            break
        else:
            print ("Opcion no valida, seleccione 'n' para NO, o 's' para SI" )

