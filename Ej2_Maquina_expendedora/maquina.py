def menu ()-> None:
    """
    La función imprime el menú de la máquina expendedora.
    """
    print("===========================")
    print("    MAQUINA EXPENDEDORA    ")
    print("===========================")
    print("    1. Agua    - $10")
    print("    2. Jugo    - $15")
    print("    3. Gaseosa - $20")
    print("===========================")
    return

def verificar_producto(producto_elegido: str) -> bool:
    """
    La función recibe el producto elegido y verifica si es válido.
    """
    if producto_elegido != "agua" and producto_elegido != "jugo" and producto_elegido != "gaseosa":
        return False
    else:
        return True

def precio(producto_elegido: str) -> int:
    """
    La función recibe el producto elegido y devuelve el precio correspondiente.
    """
    if producto_elegido == "agua":
        return 10
    elif producto_elegido == "jugo":
        return 15
    elif producto_elegido == "gaseosa":
        return 20

def verificar_dinero(dinero: int, dinero_necesario: int) -> bool:
    """
    La función confirma si el dinero ingresado es suficiente para comprar el producto.
    """
    if dinero < dinero_necesario:
        return False
    else:
        return True
    
def vuelto (dinero: int, dinero_necesario: int) -> int:
    """
    La función calcula el vuelto que se le debe dar al cliente.
    """
    return dinero - dinero_necesario

def faltante (dinero: int, dinero_necesario: int) -> int:
    """
    La función calcula el dinero que falta para completar la compra.
    """
    return dinero_necesario - dinero