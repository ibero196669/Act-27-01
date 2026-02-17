import math

class Ejercicio3():
    def __init__(self):
        self.palabra = ""
        self.adivina = "adivina"   # palabra buscada

    def leerDatos(self):
        print(" Adivina la palabra ")

    def adivinarpalabra(self):
        while True:
            self.palabra = input("Palabra: ")
            if self.palabra == self.adivina:
                print("¡Correcto!")
                break
            else:
                print("Incorrecto")