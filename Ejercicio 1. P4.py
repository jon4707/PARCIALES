
tarjetas_p={
    "T001": {"compras":3, "saldo":1500},
    "T002": {"compras":0, "saldo":3000},
}
def agregar_tarjeta_p(compras: dict, saldo: str, datos: str)->bool:
    if datos in tarjetas_p:
        tarjetas_p(datos) = {
            "compras": compras,
            "saldo": saldo
        }
        return True
    return False
def usar_tarjeta_p(compras:dict,datos: str, monto:int,)->bool:
        print(tarjetas_p(datos))
        try:
            tarjeta_nueva=int(input("INGRESE SU TARJETA:  "))
        except ValueError:
            print("ingrese una tarjeta valida por favor...")
            return False
        else:
            if monto>tarjetas_p(datos)["saldo"]:
                print("Saldo insuficiente, la compra no se puede realizar")
                return False
            else:
                tarjetas_p(datos)["saldo"]-=monto
                print("COMPRA EXITOSA")
                tarjetas_p(datos)["compra"]+=1
                return True
def listar()->None:
    if len(tarjetas_p) < 1:
        print("No exixsten tarjetas registradas.")
    else:
        print("ERROR")
            
def ver_saldo_critico(compras: dict,saldo:int)->None:
    if tarjetas_p in saldo:
        saldo>1
        print(f"las siguientes tarjetas estan en saldo critico.{tarjetas_p}")
    else:
        print(f"Las siguientes tarjetas estan fuera de estado critico.{tarjetas_p}")
        return True
    return False
    
menu_principal=True
while menu_principal:
    print("°°MENU°°")
    print("OPCIONES:")
    print("1) INGRESAR TARJETA NUEVA.")
    print("2) USAR TARJETA.")
    print("3) MOSTRAR LISTA DE TARJETAS REGISTRADAS.")
    print("4) REVISAR.")
    try:
        opc=int(input("Ingresa una opccion..."))
    except ValueError:
        print("SE ENCONTRO UN ERROR.")
    else:
        if opc==1:
            try:
                ingresa_tu_compra=int(input("INGRESA LAS COMPRAS.."))
                ingresa_tu_saldo=int(input("INGRESA TU SALDO..."))
                ingresa_tu_dato=input("ingresa el codigo de tu tarjeta...")
            except ValueError:
                print("ingrese valores validos...")
            else:
                if ingresa_tu_compra < 0 or ingresa_tu_saldo < 0:
                    print("ingrese valores validos...")
                else:
                    agregar_tarjeta_p