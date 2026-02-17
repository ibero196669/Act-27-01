import math

class Ejercicio4():
    def __init__(self):
        self.n = 0          # profundidad del pozo
        self.u = 0          # energía (sube)
        self.d = 1          # baja 1 pulgada
        self.ascenso = 0
        self.tiempo = 0

    def leerDatos(self):
        self.n = int(input("Profundidad del pozo (pulg) = "))
        self.u = int(input("Energía (pulg/min) = "))
        self.ascenso = 0
        self.tiempo = 0

    def realizarCalculo(self):
        while True:
            self.ascenso += self.u      # sube
            self.tiempo += 1            # tiempo de subida

            if self.ascenso >= self.n:  # si sale del pozo
                break

            self.ascenso -= self.d      # baja
            self.tiempo += 1            # tiempo de bajada

    def mostrarResultado(self):
        print("Tiempo en salir:", self.tiempo)


