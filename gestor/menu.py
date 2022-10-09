import os
from ejercicio4 import ejercicio_43
from ejercicio3 import ejercicio31
from ejercicio2 import ejercicio22

def iniciar():
    while True:
        os.system('clear') # cls en Windows
        print("========================")
        print(" BIENVENIDO AL Examen ")
        print("========================")
        print("[1] Ejercicio 1 ")
        print("[2] Ejercicio 2 ")
        print("[3] Ejercicio 3 ")
        print("[4] Ejercicio 4 ")
        print("[5] Salir")
        print("========================")
        opcion = input("> ")
        os.system('clear') # cls en Windows

        if opcion == '1':
            pass
        elif opcion == '2':
            print("========================")
            print(" BIENVENIDO AL EJERCICIO 2 ")
            print("========================")
            print("[1] Ejercicio 2.1 ")
            print("[2] Ejercicio 2.2 ")
            opcion = input("> ")
            if opcion=='2.2':
                ejercicio22.get_infromation22()
        elif opcion == '3':
            print("========================")
            print(" BIENVENIDO AL EJERCICIO 3 ")
            print("========================")
            print("[1] Ejercicio 3.1 ")
            print("[2] Ejercicio 3.2 ")
            opcion = input("> ")
            if opcion=='3.2':
                ejercicio31.get_information_31()

        elif opcion == '4':
            print("========================")
            print(" BIENVENIDO AL EJERCICIO 4 ")
            print("========================")
            print("[1] Ejercicio 4.1 ")
            print("[2] Ejercicio 4.2 ")
            print("[3] Ejercicio 4.3 ")
            print("[4] Ejercicio 4.4 ")
            opcion = input("> ")
            if opcion=='4.3':
                ejercicio_43.get_datos43()

        elif opcion == '6':
            print("Saliendo...\n")
            break

        input("\nPresiona ENTER para continuar...")


iniciar()

