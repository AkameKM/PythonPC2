###################### Problema 9 #########################

def sacar_vocales(texto):
    vocales = "aeiouAEIOU"
    resultado = ""
    for index in texto:
        if index not in vocales:
            resultado += index
    return resultado

frase = input("Ingrese una frase: ")

print(f"Texto sin vocales: {sacar_vocales(frase)}")
