"""
Autor:Nicolas Zabala Castaneda
Fecha: 8/12/2025
Descripcion: 
"""
#Importacion de modulos y librerias nesesarias 
import  os 
import time
import random 

#Iniciacion de las variables y diccionarios globales 
#Debe contener dos subdiccionarios, uno de contacto y otro de direcciones 
usuarios={}
productosDisp={}
cuentasClientes={}
#Es un subdiccionario por cada uno de los productos
productosClientes={}
#Historial de los movimientos de las cuentas 
histMov={}

#Definicion de las funciones que se van a usar junto a los menus
def clr():
    os.system('cls' if os.name == 'nt' else 'clear')
      
def NuevaCuenta(): 
    global usuarios
    global cuentasClientes
    llave = len(usuarios)+1
    while True:
        clr()
        print("Para crear una cuenta nueva, porfavor ingrese los siguientes datos")       
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
                    nuevaC = False
                    continue
                case "S":
                    break
                case _:
                    input("Valor no soportado\nIngrese un valor valido")
        
       
#Captar cc            
def CC():
    clr()
    while True:
     cc = input("Dijite su numero de identificacion personal")
            
     if cc in usuarios:
        input("Este numero ya se encuentra registrado, intente con otro  \nOprima una tecla para continuar")
     else:
        return cc           
#Captar nombre            
def Nombre():
    while True:
        clr()
        nombre = input("Porfavor ingrese el nombre del titular de la cuenta")
        if nombre.isalpha():
            return nombre
        else:
            input("El nombre solo debe contener caracteres alfabeticos \nPresione una tecla para continuar")
#Captar email
def Email():
    while True:
        clr()
        email = input("Porfavor ingrese su email")
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
     edad=int(input("Porfavor ingrese la edad del titular de la cuenta"))
     if edad < 17:
         print("lo sentimos no puede crear una cuenta para menores de edad")  
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
                    fijo = input("Ingrese su numero de telefono fijo")
                    if fijo.isdigit() and len(fijo) == 7:
                        return fijo
                    else:
                        input("El fijo debe contener solo numeros y debe ser de 7 digitos")
                case "2":
                    mov = input("Ingrese su numero telefonico")
                    if mov.isdigit() and len(mov) == 10:
                        return mov
                    else:
                        input("El numero telefonico debe contener solo numeros y debe ser de 10 digitos")
                case "3":
                    input("Lo sentimos no puede crear una cuenta con ambos numeros elija unos solo \nOprima una tecla para continuar")
                    return False
                case "4":
                    input("Lo sentimos no puede crear una cuenta sin un numero añadido \nOprima una tecla para continuar")
                    return False
                case _: 
                    input("Elija una de las opciones validas porfavor \nOprima una tecla para continuar")
                    break   
#Capta ubi
def Ubicacion():
    while True:
        clr()
        ubicacion = {}
        ubicacion.update({"Pais": input("Ingrese el pais en el que reside actualmente").upper()})
        ubicacion.update({"Departamento": input("Ingrese su departamento de residencia").upper()}) 
        ubicacion.update({"Ciudad": input("Ingrese su ciudad de residencia").upper()}) 
        ubicacion.update({"Dia": input("Ingrese su direccion de residencia").upper()})
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
        str(input("Porfavor indique el tipo de cuenta que desea crear (Ahorros/Corriente/Ambas): ").upper())
        match input: 
            case "AHORROS":
                id1= random.randint(100,999)
                cu={{"AHORROS": id1,"SALDO":0}}
                cuentas.update({1:cu})
                input("Ha seleccionado una cuenta de ahorros\nOprima una tecla para continuar")
                return cuentas
            case "CORRIENTE":
                id1= random.randint(100,999)
                cu={{"CORRIENTE": id1,"SALDO":0}}
                cuentas.update({1:cu})
                input("Ha seleccionado una cuenta corriente\nOprima una tecla para continuar")
                return cuentas
            case "AMBAS":
                id1= int(random.randint(100,999))
                id2= int(random.randint(100,999))
                if id1 == id2:
                    id2= int(random.randint(100,999))
                else:
                    pass
                cu1 = {"AHORROS": id1,"SALDO":0}
                cu2 = {"CORRIENTE": id2,"SALDO":0}
                cuentas.update({1:cu1, 2:cu2})
                input("Ha seleccionado ambas cuentas\nOprima una tecla para continuar")
                return cuentas
            case _:
                input("Opcion no valida\nOprima una tecla para continuar")
def Depositar():
    global usuarios
    idfcc=str(input("Para hacer un deposito porfavor ingrese el numero de cedula de su cuenta"))
    for i, cc in usuarios.items:
        if idfcc == cc.get("CC"):
            cu=usuarios.get("CUENTAS") 
            print(f"La cedula se encuentra registrada, y estas son las cuentas asociadas a dicha cedula:{cu}")
        else:
            pass
    idf=str(input("Ahora porfavor ingrese el numero de la cuenta a la que desea depositarle el dinero"))
    montoD=int(input("Ahora porfavor ingrese el monto que dese depositar en la cuenta"))
    for i, cuent in usuarios.items:
        if idf == cuent.items:
    pass

def SolicitarProducto(): 
    pass 
def Pagodesaldo():
    pass
def Saldopendiente():
    pass
def EliminarCuenta():
    pass 
def MenuInicio():
    print("Elija una de las siguientes opciones porfavor")
    opcion = str(input("""
                        1. Crear nueva cuenta 
                        2. Depositar dinero 
                        3. Retirar dinero
                        4. Solicitar credito 
                        5. Pago cuota credito 
                        6. Eliminar cuenta
                        7. Salir
                         """))
    return opcion

def MenuProductos():
    pass

#Maquetacion de los menus que se van a formar

print("Bienvenido al programa del sistema bancario")
time.sleep(1)

while True: 
    op = MenuInicio()
