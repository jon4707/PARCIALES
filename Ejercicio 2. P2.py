import random
print("Bienvenido... Adivina la temperatura")
tem_min=int(input("Ingresa tu temperatura minima"))
tem_max=int(input("ingresa tu temperatura maxima"))

tem=random.randint(tem_min, tem_max)

intentos=int(input("tines 3 intentos, TU PUEDES..."))

intento1=int(input("Intento 1: Adivina la temperatura:  "))
if intento1==tem:
    print("CORRECTO, ADIVINASTE EL NUMERO...")
else:
    if intento1 < tem:
        print("La temperatura es mayor")
    else: 
        print("La temperatura es menor")
        
intento2=int(input("Intento 2: Adivina la temperatura:  "))
if intento2==tem:
    print("CORRECTO, ADIVINASTE EL NUMERO...")
else:
    if intento2 < tem:
        print("La temperatura es mayor")
    else: 
        print("La temperatura es menor")
        
intento3=int(input("Intento 3: Adivina la temperatura:  "))
if intento3==tem:
    print("CORRECTO, ADIVINASTE EL NUMERO...")
else:
    if intento3 < tem:
        print("La temperatura es mayor")
    else: 
        if print("La temperatura es menor")
        else:
            print("no adivinaste el numero")