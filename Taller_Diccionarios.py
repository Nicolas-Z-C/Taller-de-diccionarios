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
usuarioDatos = {}
productosDisp = {}
#Es un subdiccionario por cada uno de los productos
productosCliente = {}
#Historial de los movimientos de las cuentas 
histMov = {}

#Definicion de las funciones que se van a usar junto a los menus
def clr():
    pass 
def NuevaCuenta():        
    pass 
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
