###################### Problema 7 #########################
def num_divisores(num):
    divisores = []
    for i in range(1, num):
        if num % i == 0:
            divisores.append(i)
    return divisores

def num_perfecto(num):
    return sum(num_divisores(num)) == num

def numeros_perfectos_menores_1000():
    perfectos = []
    for num in range(1, 1000):
        if num_perfecto(num):
            perfectos.append(num)
    return perfectos

perfectos = numeros_perfectos_menores_1000()
print(f"Los números perfectos menores que 1000 son: {perfectos}")
