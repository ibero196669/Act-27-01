from Ejercicios.ejercicio1 import ejercicio_1
from Ejercicios.ejercicio2 import ejercicio_2
from Ejercicios.ejercicio3 import ejercicio_3
from Ejercicios.ejercicio4 import ejercicio_4
from poo.clases.ejercicio1_poo import Ejercicio1
from poo.clases.ejercicio2_poo import Ejercicio2


def menu_principal():
    while True:
        print("Menú principal")
        print("1. Ejercicio 1")
        print("2. Ejercicio 2")
        print("3. Ejercicio 3")
        print("4. Ejercicio 4")
        print("5. Salir")
        op=int(input("Eliga una opción: "))
        match(op):
            case 1:
                #ejercicio_1()
                test = Ejercicio1()
                test.leerDatos()
                test.realizarCalculo()
                test.mostrarResultado()

            case 2:
                #ejercicio_2()
                test = Ejercicio2()
                test.leerDatos()
                test.realizarCalculo()

            case 3:
                ejercicio_3()
            case 4:
                ejercicio_4()
            case 5:
                break
            case _:
                print("Opción no válida")