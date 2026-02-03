import math
def ejercicio_1():

    x = float(input("x="))
    tolerancia = float(input("Tolerancia="))
    valorReal = math.sin(x)
    k = 0
    aprox = 0
    while True:
        aprox += ((-1)**k*x**(2*k+1))/math.factorial(2*k+1)
        k += 1
        error = math.fabs((valorReal - aprox)/valorReal) * 100
        if error < tolerancia:
            break

    print("Valor real = ", valorReal)
    print("Aproximación = ", aprox)
    print("Error = ",error)