"""
Autor:Nicolas Zabala Castaneda
Fecha: 8/12/2025
Descripcion: 
"""
#Importacion de modulos y librerias nesesarias 
import  os 
import datetime
import time
import random 

#Iniciacion de las variables y diccionarios globales 
#Debe contener dos subdiccionarios, uno de contacto y otro de direcciones 
usuarios={}
#Es un subdiccionario por cada uno de los productos
cuentasClientes={}
productosClientes={}
#Historial de los movimientos de las cuentas 
histMov={}

#Definicion de las funciones que se van a usar junto a los menus
def clr():
    os.system('cls' if os.name == 'nt' else 'clear')
      
def NuevaCuenta(): 
    global usuarios
    global cuentasClientes
    while True:
        llave = len(usuarios)
        clr()
        print(usuarios)
        input("Para crear una cuenta nueva, porfavor ingrese los datos que se iran pidiendo a continuacion\nOprima una tecla para continuar")       
        nomus=Nombre().upper()
        ccus=CC()
        email=Email().upper()
        edad=Edad()
        contacto=Telefono()
        ubi=Ubicacion()
        tipoCuenta = CuentaPlata()
        nuevousr = {"Nombre":nomus,"CC":ccus,"EMAIL":email,"EDAD":edad,"CONTACTO":contacto,"UBICACION":ubi}
        cuentasClientes.update({ccus:tipoCuenta})  
        usuarios.update({llave+1:nuevousr})
        op = input("Proceso Finalizado correctamente\nDesea crear una nueva cuenta?(S|N)").upper()
        nuevaC = True
        while nuevaC:
            match op:
                case "N":
                    return
                case "S":
                    break
                case _:
                    input("Valor no soportado\nIngrese un valor valido")
        
       
#Captar cc            
def CC():
    clr()
    while True:
     cc = input("Dijite su numero de identificacion personal: ")

     for i in usuarios.values():
         if i["CC"] == cc:
             input("Este numero ya se encuentra registrado, intente con otro  \nOprima una tecla para continuar")
             break
     else:
        return cc           
#Captar nombre            
def Nombre():
    while True:
        clr()
        nombre = input("Porfavor ingrese el nombre del titular de la cuenta: ")
        if nombre.isalpha():
            return nombre
        else:
            input("El nombre solo debe contener caracteres alfabeticos \nPresione una tecla para continuar")
#Captar email
def Email():
    while True:
        clr()
        email = input("Porfavor ingrese su email: ")
        if "@gmail.com" or "@hotmail.com" in email: 
            pass
        else:
            input("Ingrese un correo electronico valido porfavor, recuerde solo se aceptan @gmail o @hotmail \nOprima una tecla para continuar")
        if email in usuarios:
            input("Este email ya se encuentra registrado, intente con otro \nOprima una tecla para continuar")
        else:
            return email  
#Captar Edad
def Edad():
    while True:
     clr()   
     edad=int(input("Porfavor ingrese la edad del titular de la cuenta: "))
     if edad < 18:
         input("lo sentimos no puede crear una cuenta para menores de edad\nOprima una tecla para continuar")
         continue
     else:
         return edad   
#captar telefono
def Telefono():
    while True:
        clr()
        print("Ingrese una de las siguientes opciones para su telefono")
        op = input("""
                   1. Fijo
                   2. Celular
                   3. Ambos
                   4. Ninguno
                   """)
        while True:
            match op:
                case "1":
                    fijo = input("Ingrese su numero de telefono fijo: ")
                    if fijo.isdigit() and len(fijo) == 7:
                        return fijo
                    else:
                        input("El fijo debe contener solo numeros y debe ser de 7 digitos")
                case "2":
                    mov = input("Ingrese su numero telefonico: ")
                    if mov.isdigit() and len(mov) == 10:
                        return mov
                    else:
                        input("El numero telefonico debe contener solo numeros y debe ser de 10 digitos")
                case "3":
                    input("Lo sentimos no puede crear una cuenta con ambos numeros elija uno solo \nOprima una tecla para continuar")
                    break
                case "4":
                    input("Lo sentimos no puede crear una cuenta sin un numero añadido \nOprima una tecla para continuar")
                    break
                case _: 
                    input("Elija una de las opciones validas porfavor \nOprima una tecla para continuar")
                    break   
#Capta ubi
def Ubicacion():
    while True:
        clr()
        ubicacion = {}
        ubicacion.update({"Pais": input("Ingrese el pais en el que reside actualmente: ").upper()})
        ubicacion.update({"Departamento": input("Ingrese su departamento de residencia: ").upper()}) 
        ubicacion.update({"Ciudad": input("Ingrese su ciudad de residencia: ").upper()}) 
        ubicacion.update({"Dia": input("Ingrese su direccion de residencia: ").upper()})
        for i, val in ubicacion.items():
            if val.isalpha() and not val.isdigit():
                return ubicacion
            else:
                print(f"Error, el dato ingresado en {i} es incorrecto")
def CuentaPlata():
    clr()
    print("Para finalizar el proceso debe crear una cuenta de ahorros o corriente")
    while True:
        cuentas={}
        op=str(input("Porfavor indique el tipo de cuenta que desea crear (Ahorros/Corriente/Ambas): ").upper())
        match op: 
            case "AHORROS":
                cu={"TIPOCUENTA":"AHORROS","SALDO":0}
                cuentas.update({1:cu})
                input("Ha seleccionado una cuenta de ahorros\nOprima una tecla para continuar")
                return cuentas
            case "CORRIENTE":
                cu={"TIPOCUENTA":"CORRIENTE","SALDO":0}
                cuentas.update({1:cu})
                input("Ha seleccionado una cuenta corriente\nOprima una tecla para continuar")
                return cuentas
            case "AMBAS":
                cu1 = {"TIPOCUENTA":"AHORROS","SALDO":0}
                cu2 = {"TIPOCUENTA":"CORRIENTE","SALDO":0}
                cuentas.update({1:cu1, 2:cu2})
                input("Ha seleccionado ambas cuentas\nOprima una tecla para continuar")
                return cuentas
            case _:
                input("Opcion no valida\nOprima una tecla para continuar")
def Depositar():
        global cuentasClientes
        usdeseado=str(input("Ingrese el numero de cedula del titular de la cuenta a la que desea depositar: "))
        for i in usuarios.values():
            if i["CC"] == usdeseado:
                tipoCuenta=str(input("Ahora porfavor ingrese el tipo de cuenta a la que desea depositar(AHORROS|CORRIENTE): ").upper())
                while True:
                    montoDepo=int(input("Ingrese el monto a depositar en la cuenta, sin espacios, puntos o comas: "))
                    if montoDepo < 0:
                        input("Valor no soportado porfavor vuelva a intentarlo\nOprima una tecla para continuar")
                    for i, r in cuentasClientes.items():
                        try:
                            if usdeseado in i:
                                for f, x in r.items():
                                    if tipoCuenta in x.values():
                                            x["SALDO"] += montoDepo
                                            print(f"El valor final de la cuenta es de:{x}")
                                            return
                                    else:
                                        pass
                            else:
                                pass
                        except:
                            pass
            else:
                pass
        input("El numero de cedula ingresado no se encuentra en nuestro sistema\nOprima una tecla para continuar")
def Retirar():
    global cuentasClientes
    usdeseado=str(input("Ingrese el numero de cedula del titular de la cuenta a la que desea retirar"))
    for i in usuarios.values():
        if i["CC"] == usdeseado:
            tipoCuenta=str(input("Ahora porfavor ingrese el tipo de cuenta a la que desea retirar(AHORROS|CORRIENTE)").upper())
            while True:
                montoRet=int(input("Ingrese el monto a retirar de la cuenta, sin espacios, puntos o comas"))
                if montoRet < 0:
                    input("Valor no soportado porfavor vuelva a intentarlo\nOprima una tecla para continuar")
                for i, r in cuentasClientes.items():
                    try:
                        if usdeseado in i:
                            for f, x in r.items():
                                if tipoCuenta in x.values():
                                        if montoRet > x["SALDO"]:
                                            input("No se puede retirar más de lo que hay en la cuenta\nOprima una tecla para continuar")
                                            continue
                                        else:
                                            x["SALDO"] -= montoRet
                                            print(f"El valor final de la cuenta es de:{x}")
                                            return
                                else:
                                    pass
                        else:
                            pass
                    except:
                        pass
        else:
             pass
    input("El numero de cedula ingresado no se encuentra en nuestro sistema\nOprima una tecla para continuar")

def SolicitarProducto(): 
    clr()
    global productosClientes
    productos={}
    ccus = str(input("Para continuar, ingrese su numero de cedula porfavor: "))
    for i in usuarios.values():
        if i["CC"] == ccus:
            while True:
                llave = len(productos)
                print("Porfavor elija una de las opciones descritas abajo, porfavor solo dijite el numero: ")
                opm = MenuProductos()    
                match opm  :
                    case "1":
                        print("Ha seleccionado el producto CDT")
                        cd={"TIPOPRODUCTO":"CDT","ID":random.randint(100,9999),"FECHA_CREACION":datetime.datetime.now(),"ESTATUS":"ACTIVO","SALDO":50000}
                        productos.update({llave+1:cd})
                        productosClientes.update({ccus:productos})
                        input("Se ha creado el CDT correctamente\nOprima una tecla para continuar")
                        op = input("Desea agregar un nuevo producto?(S|N)").upper()
                        if op == "S":
                            continue
                        else:
                            return 
                    case "2":   
                        print("Ha seleccionado el producto Credito libre inversion")
                        cli={"TIPOPRODUCTO":"CREDITOLIBREINVERSION","ID":random.randint(100,9999),"FECHA_CREACION":datetime.datetime.now(),"ESTATUS":"ACTIVO","SALDO_A_PAGAR":50000}
                        productos.update({llave+1:cli})
                        productosClientes.update({ccus:productos})
                        input("Se ha creado el Credito libre inversion correctamente\nOprima una tecla para continuar")
                        op = input("Desea agregar un nuevo producto?(S|N)").upper()
                        if op == "S":
                            continue
                        else:
                            return 
                    case "3":
                        print("Ha seleccionado el producto Credito vivienda")
                        cv={"TIPOPRODUCTO":"CREDITOVIVIENDA","ID":random.randint(100,9999),"FECHA_CREACION":datetime.datetime.now(),"ESTATUS":"ACTIVO","SALDO_A_PAGAR":50000}
                        productos.update({llave+1:cv})
                        productosClientes.update({ccus:productos})
                        input("Se ha creado el Credito vivienda correctamente\nOprima una tecla para continuar")
                        op = input("Desea agregar un nuevo producto?(S|N)").upper()
                        if op == "S":
                            continue
                        else:
                            return 
                    case "4":
                        print("Ha seleccionado el producto Credito compra auto movil")
                        ca={"TIPOPRODUCTO":"CREDITOCOMPRAAUTOMOVIL","ID":random.randint(100,9999),"FECHA_CREACION":datetime.datetime.now(),"ESTATUS":"ACTIVO","SALDO_A_PAGAR":50000}
                        productos.update({llave+1:ca})
                        productosClientes.update({ccus:productos})
                        input("Se ha creado el Credito compra auto movil correctamente\nOprima una tecla para continuar")
                        op = input("Desea agregar un nuevo producto?(S|N)").upper()
                        if op == "S":
                            continue
                        else:
                            return 
                    case _:
                        print("Opcion no valida")
        else:
            pass
    input("El numero de cedula ingresado no se encuentra en nuestro sistema\nOprima una tecla para continuar")

def Pagodesaldo():
    global productosClientes
    usdeseado=str(input("Ingrese el numero de cedula del titular del producto al que desea pagar el saldo: "))
    for i in usuarios.values():
        if i["CC"] == usdeseado:
            tipoSaldo=str(input("Ahora porfavor ingrese el tipo de producto al que desea pagar el saldo, todo pegado como a continuacion(CDT|CREDITOLIBREINVERSION|CREDITOVIVIENDA|CREDITOCOMPRAAUTOMOVIL): ").upper().strip())
            while True:
                montoDepo=int(input("Ingrese el monto a pagar del saldo, sin espacios, puntos o comas: "))
                if montoDepo < 0:
                    print("Valor no soportado porfavor vuelva a intentarlo")
                else:
                    pass              
                for i, r in productosClientes.items():
                    try:
                        if usdeseado in i:
                            for f, x in r.items():
                                if tipoSaldo in x.values():
                                        if montoDepo > x["SALDO_A_PAGAR"]:
                                            input("No se puede pagar más de lo que hay en el saldo pendiente\nOprima una tecla para continuar")
                                            continue
                                        elif montoDepo == x["SALDO_A_PAGAR"]:
                                            x["ESTATUS"] = "PAGADO"
                                            x["SALDO_A_PAGAR"] = 0
                                            input("El saldo ha sido pagado por completo\nOprima una tecla para continuar")
                                        else:
                                            x["SALDO_A_PAGAR"] -= montoDepo
                                            print(f"El valor final del credito es de:{x}")
                                            return
                                else:
                                    pass
                        else:
                            pass
                    except:
                        pass
        else:
             pass
    input("El numero de cedula ingresado no se encuentra en nuestro sistema\nOprima una tecla para continuar") 

def Saldopendiente():
    global productosClientes
    usdeseado=str(input("Ingrese el numero de cedula del titular del los productos que desea visualizar"))
    for i in usuarios.values():
        if i["CC"] == usdeseado:
            for j, k in productosClientes.items():
                if i["CC"] in j:
                    print(f"Productos del usuario con cc: {usdeseado}")
                    for l, m in k.items():
                        print(f" - {m['TIPOPRODUCTO']}: {m['SALDO_A_PAGAR']}")
                    input("Oprima una tecla para continuar")
                    return
                else:
                    pass 
    input("El numero de cedula ingresado no se encuentra en nuestro sistema\nOprima una tecla para continuar") 

def EliminarCuenta():
    global productosClientes
    print("El procedimiento que va a realizar es completamente irreversible, todas las cuentas seran eliminadas")
    op = input("Desea continuar?(S|N)").upper()
    if op == "S":
        usuarios.clear()
        cuentasClientes.clear()
        productosClientes.clear()
        input("Se han eliminado todos los usuarios y cuentas del sistema correctamente\nOprima una tecla para continuar")
    else:
        input("El procedimiento ha sido cancelado\nOprima una tecla para continuar")
        return
def MenuInicio():
    opcion = str(input(""" Elija una de las siguientes opciones porfavor
                        1. Crear nueva cuenta 
                        2. Depositar dinero 
                        3. Retirar dinero
                        4. Solicitar credito 
                        5. Pago cuota credito 
                        6. Visualizar mis productos
                        7. Eliminar cuenta
                        8. Salir
                    """))
    return opcion

def MenuProductos():
   print("Elija uno de los siguientes productos porfavor")
   opcion= input("""
    1.CDT
    2.Credito libre inversion
    3.Credito viviendia
    4.Credit compra auto movil
    """)
   return opcion

#Maquetacion de los menus que se van a formar
print("Bienvenido al programa del sistema bancario")
time.sleep(1)

while True: 
    
    op = MenuInicio()
    match op:
        case "1":
            NuevaCuenta()
        case "2":
            Depositar()
        case "3":
            Retirar()
        case "4":
           SolicitarProducto()
        case "5":
            Pagodesaldo()
        case "6":
            Saldopendiente()
        case "7":
            EliminarCuenta()
        case "8":
            print("Gracias por usar el sistema bancario")
            exit()
        case _:
            print("Opcion no valida")


    
