

############# Problema 1 ############


def numeros():
    for index in range(1500, 2701):
        if index % 5 == 0 and index % 7 == 0:
          print(f"{index} es multiplo de 5 y divisible de 7")
numeros()


