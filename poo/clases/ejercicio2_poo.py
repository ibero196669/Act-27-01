class Ejercicio2():
    def __init__(self):
        self.password = ""
        self.intentos = 0
        self.palabra = ""

    def leerDatos(self):
        self.password = "lunes"
        self.intentos = 0
        self.palabra = ""

    def realizarCalculo(self):
        while self.palabra != self.password:
            self.palabra = input("Contraseña:")
            self.intentos += 1
            if self.intentos == 5:
                print("Excediste las oportunidades")
                break