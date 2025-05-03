# Muestra el menú y controla el flujo del programa llamando a las funciones del módulo puerta.py
from puerta import (menu_principal, 
                    estado_puerta, 
                    abrir_puerta, 
                    cerrar_puerta, 
                    cambiar_clave)
clave_correcta = "1234" 
estado = False 
opcion = ""

print("Bienvenido al simulador de puerta secreta")
while opcion != "5":
    print("========================================")
    print( menu_principal() )
    print("========================================")

    opcion = input("Elige una opción (número): ")
    match opcion:
        case "1":
            print(estado_puerta(estado))

        case "2":
            clave = input("Introduce la clave para abrir la puerta: ")
            abrir = abrir_puerta(estado, clave, clave_correcta)
            print(abrir)
            if abrir == "Clave incorrecta. La puerta no se ha abierto.":
                estado = False
            else:
                estado = True

        case "3":
            print(cerrar_puerta(estado))
            estado = False

        case "4":
            clave = input("Introduce la clave actual: ")
            cambio = cambiar_clave(clave, clave_correcta)
            if cambio == True:
                nueva_clave = input("Introduce la nueva clave: ")
                clave_correcta = nueva_clave
                print("Clave cambiada con éxito.")
            else:
                print("Clave incorrecta. No se ha cambiado la clave.")

        case "5":
            print("Saliendo del programa...")

        case _:
            print("Opción no válida. Inténtalo de nuevo.")

print("Fin del programa.")
