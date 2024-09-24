
"""
Problema 1:
Escribe un programa en Python para encontrar los números que son divisibles por 7 y múltiplos de 5,
en el rango de 1500 y 2700 (ambos incluidos). 
"""


def numeros():
    for index in range(1500, 2701):
        if index % 5 == 0 and index % 7 == 0:
          print(f"{index} es multiplo de 5 y divisible de 7")
numeros()


