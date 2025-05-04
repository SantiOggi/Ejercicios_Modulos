def pedir_temperatura()-> int:
    """
    La función pide al usuario que ingrese una temperatura 
    entre -100 y 100°C inclusive.
    """
    temperatura_ingresada = int(input("Ingrese la temperatura: "))
    while temperatura_ingresada < -100 or temperatura_ingresada > 100:
        print("Temperatura no válida. Debe estar entre -100 y 100°C.")
        temperatura_ingresada = int(input("Ingrese la temperatura: ")) 
    return temperatura_ingresada

def mostrar_temperatura(temperatura: int) -> None:
    """
    La función muestra la temperatura ingresada por el usuario.
    """
    print(f"La temperatura ingresada es: {temperatura}°C")