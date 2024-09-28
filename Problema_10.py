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
