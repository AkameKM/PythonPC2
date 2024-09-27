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