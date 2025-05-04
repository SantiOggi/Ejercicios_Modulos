def es_temperatura_segura(temperatura: int) -> bool:
    """
    La función verifica si la temperatura ingresada es segura.
    """
    if -20 <= temperatura <= 5:
        return True
    else:
        return False

def mostrar_estado(temperatura: int) -> None:
    """
    La función muestra si la temperatura ingresada es segura.
    """
    if es_temperatura_segura(temperatura):
        print("La temperatura es segura.")
    else:
        print("La temperatura es peligrosa.")