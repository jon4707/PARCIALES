#Desarrolla un programa en Python que permita
# calcular el subsidio de luz según el quintil 
# al que pertenece la familia del solicitante y su condición laboral.
#Condiciones socioeconómicas:
#•	Quintil de ingresos: 
# Hay 5 quintiles en total (1 = menores ingresos, 5 = mayores in-gresos).
#•	Condición laboral: Se considera si la persona está desempleada o empleada.

#Quintil	Condición Laboral	Subsidio de Luz
#1 o 2	Desempleado	$50.000
#1 o 2	Empleado	$40.000
#3	Desempleado	$30.000
#3	Empleado	$20.000
#En caso de que el solicitante no cumpla
# con ninguno de los requisitos anteriores entonces NO HAY SUBSIDIO DE LUZ.
#Bonos Adicionales:
#•	Si el solicitante pertenece al Quintil 1 o 2,
# recibe un bono adicional de $10.000. 
# Si además es mayor de 65 años, recibe $20.000 extra.
#•	En cualquier otro caso el bono adicional es CERO.
#Ejemplo 1:
#Ingrese su quintil (1-5): 1
#Ingrese su condición laboral (empleado/desempleado): desempleado
#Ingrese su edad: 70
#El valor del subsidio de luz es: 80.000
c_laboral=input("ingrese si es empleado o desempleado:  ")
quintinil=input("selecicone su quintinil:  ")
edad=int(input("indique su edad:  "))

subsidio=0

if c_laboral== "empleado":
    
    if quintinil=="1" or "2":
        print("su subsidio de la luz es de $40.000")
        subsidio=40000
    else:
        if quintinil==("3"):
            print("su subsidio de la luz es de $20.000")
            subsidio=20000


if c_laboral== "desempleado":
    
    if quintinil=="1" or "2":
        print("su subsidio de la luz es de $50.000")
    else:
        if quintinil==("3"):
            print("su subsidio de la luz es de $30.000")
            
bono=0
if quintinil== "1" or "2":
    bono+=10000
if edad>65:
    bono+=20000
else:
    bono+=0

if subsidio >0:
    print(f"Su subsidio de la luz es de:  ${subsidio}")
    if bono > 0:
        print(f"bono adicional: ${bono}")
        print(f"total: ${subsidio + bono}")
    else:
        print("no tiene subsidio de la luz...")

