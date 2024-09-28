###################### Problema 5 #########################
def num_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_primos_menores_100():
    suma = 0
    for num in range(2, 100):
        if num_primo(num):
            suma += num
    return suma

resultado = sum_primos_menores_100()
print(f"La suma de los números primos menores que 100 es: {resultado}")
