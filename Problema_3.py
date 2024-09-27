###################### Problema 3 #########################

numeros= []
pares = 0
impares = 0

while True:
    repuesta = input("¿Desea ingresar un número? (SI/NO): ").upper()

    if repuesta == "SI":
        numero = int(input("Ingrese número: "))
        numeros.append(numero)

        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    else:
        break
    
print(f"Números ingresados: {numeros}")
print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")