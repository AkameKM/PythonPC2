###################### Problema 8 #########################
def factorial(n):
    if n < 0:
        return "El número debe ser un entero no negativo."
    elif n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado
num = int(input("Ingrese numero: "))
print(f"El factorial de {num} es: {factorial(num)}")
