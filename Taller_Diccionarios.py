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
usuarios= {}
productosDisp= {}
#Es un subdiccionario por cada uno de los productos
productosClientes= {}
#Historial de los movimientos de las cuentas 
histMov= {}

#Definicion de las funciones que se van a usar junto a los menus
def clr():
    os.system('cls' if os.name == 'nt' else 'clear')
      
def NuevaCuenta(): 
    global usuarios
    CC = True
    while True:
        print("Para crear una cuenta nueva, porfavor ingrese los siguientes datos")       
        nomus=Nombre()
        ccus=CC()
        
       
#Captar cc            
def CC():
 
    while True:
     cc = input("Dijite su numero de identificacion personal")
            
     if cc in usuarios:
        input("Este numero ya se encuentra registrado, intente con otro  \nOprima una tecla para continuar")
     else:
        return cc           
#Captar nombre            
def Nombre():
    while True:
        #Nombre
        nombre = input("Porfavor ingrese el nombre del titular de la cuenta")
        if nombre.isalpha():
            return nombre
        else:
            input("El nombre solo debe contener caracteres alfabeticos \nPresione una tecla para continuar")
#Captar email
def Email():
    while True:
        email = input("Porfavor ingrese su email")
        if "@gmail.com" or "@hotmail.com" in email: 
            pass
        else:
            input("Ingrese un correo electronico valido porfavor, recuerde solo se aceptan @gmail o @hotmail \nOprima una tecla para continuar")
        if email in usuarios:
            input("Este email ya se encuentra registrado, intente con otro \nOprima una tecla para continuar")
        else:
            return email           
#captar telefono
def Telefono():
    while True:
        print("Ingrese una de las siguientes opciones para su telefono")
        op = input("""
                   1. Fijo
                   2. Celular
                   3. Ninguno
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
                    input("Lo sentimos no puede crear una cuenta sin un numero añadido \n Oprima una tecla para continuar")
                    return False
                case _: 
                    input("Elija una de las opciones validas porfavor \nOprima una tecla para continuar")
                    break   
#Capta ubi
def Ubicacion():
                
def Depositar():
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
