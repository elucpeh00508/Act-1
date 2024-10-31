from datetime import datetime 
año_actual = datetime.now().year 

nombre = input("Nombre del empleado: ")
empleado = int(input("""Tipo de empleado:
1. Asalariado
2. Comisionado
3. Por horas
¿Qúe tipo de empleado eres? (1-3): """))

if (empleado == 1):
    año = float(input("Año de contratación: "))
    print("Contradado desde: ",año)
    sueldo = int(1000 + 100*(año_actual-año))
    print ("Nombre: ", nombre)
    print ("Sueldo: ",sueldo,"€")
elif (empleado == 2):
    ventas = float(input("Total de ventas: "))
    print("Ventas: ",ventas)
    sueldo = int(800 + 10*ventas)
    print ("Nombre: ",nombre)
    print ("Sueldo: ",sueldo,"€")
elif (empleado == 3):
    horas = float(input("Horas trabajadas: "))
    print ("Horas trabajadas: ",horas )
    sueldo = int(8*horas)
    print ("Nombre: ", nombre)
    print ("Sueldo: ",sueldo,"€")
