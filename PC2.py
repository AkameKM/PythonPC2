############# Problema 1 ############


def numeros():
    for index in range(1500, 2701):
        if index % 5 == 0 and index % 7 == 0:
          print(f"{index} es multiplo de 5 y divisible de 7")
numeros()

#################### Problema 2 ########################
x = 7
for i in range(1,x + 1):
    print("*" * i)

for i in range(x - 1, 0, -1):
    print("*" * i)

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

################### Problema 4 #####################

list_alumnos = []

cant = int(input("Ingrese la cantidad de alummnos que va a registrar: "))

for i in range(cant):
   alumno = input(f"Ingrese el nombre del alumno {i+1}: ")
   notas = []

   for j in range(3): 
      nota = float(input(f"Ingrese la nota {j+1} de {alumno}: "))
      notas.append(nota)

   libreta = {
       "Alumno": alumno,
       "Notas": notas
    }
   
   list_alumnos.append(libreta)

print("Las calificaciones de los alumnos son: ")
for alumno in list_alumnos:
   print(f"Alumno: {alumno['Alumno']}, Notas: {alumno['Notas']}")


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

###################### Problema 6 #########################

def fibonacci():

      prev = 0
      next = 1
      while prev <=50:
          print(prev)
          fib = prev + next
          prev = next
          next = fib
   
fibonacci()


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

###################### Problema 10 #########################

def fecha_a_convertir(fecha):

    meses = {
        "Enero": "01",
        "Febrero": "02", 
        "Marzo": "03", 
        "Abril": "04",
        "Mayo": "05", 
        "Junio": "06", 
        "Julio": "07", 
        "Agosto": "08",
        "Septiembre": "09", 
        "Octubre": "10", 
        "Noviembre": "11", 
        "Diciembre": "12"
    }
    
    if '/' in fecha:
        mes, dia, anio = fecha.split('/')
        return f"{anio}-{int(mes):02}-{int(dia):02}"
    else:
        nombre_mes, dia_anio = fecha.split(' ', 1)
        dia, anio = dia_anio[:-1].split(', ')
        mes = meses[nombre_mes]
        return f"{anio}-{mes}-{int(dia):02}"

fecha = input("Ingrese una fecha (MM/DD/AAAA o 'Mes día, año'): ")

print(f"Fecha en formato AAAA-MM-DD: {fecha_a_convertir(fecha)}")