par_divisible=0
par_indivisible=0


programa_activo=True
while programa_activo:
    print("----MENU PRINCIPAL----")
    print("-A. Ingresar 2 numero.")
    print("-B. Mostrar estadisticas.")
    print("-C. Terminar programa.")
    try:
        opc=str(input("Seleccione una opcion... "))
    except ValueError:
        print("Seleccione sola una de esas opciones (A, B o C).")
    else:
        if opc=="A":
            while True:
                try:
                    num1=int(input("Ingrese un numeros entero, positivo o negativo. "))
                    num2=int(input("Ingrese el segundo numero entero, positivo o negativo. "))
                    
                    if num1%num2==0 or num2%num1==0:
                        par_divisible+=1
                        print("Estos numeros son divisibles entre si.")
                    elif num1%num2!=0 or num2%num1!=0:
                        par_indivisible+=1
                        print("Estos numeros no son divisibles entre si.")
                        
                    else:
                        print("Su opcion es invalida, vuelva a intentarlo...")
                        
                        
                except ValueError:
                    print("Seleccione una opcion valida...")
                
                
        elif opc=="B":
            print(f"La cantidad de parejas de numeros DIVISIBLES entre si son {par_divisible}, hasta el momento...")
            print(f"La cantidad de parejas de numeros NO DIVISIBLES entre si son {par_indivisible}, hasta el momento...")
            parejas_totales=par_divisible+par_indivisible
            print(f"El total de pares divisibles + loa pares no divisibles son {parejas_totales} hasta el momento...")
        elif opc=="C":
            print("AUTOR DEL PROGRAMA: Jonathan Garrido.\nSaludos.")
        programa_activo=False