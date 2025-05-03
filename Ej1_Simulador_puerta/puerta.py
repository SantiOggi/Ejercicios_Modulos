""" Módulo con funciones para:
Ver el estado de la puerta (abierta o cerrada)
Abrir la puerta (sólo si la clave es correcta)
Cerrar la puerta
Cambiar la clave (si la clave actual es correcta)
"""
def menu_principal() -> str:
    """Función que muestra el menú principal."""
    return  """1. Ver estado de la puerta
    2. Abrir puerta
    3. Cerrar puerta
    4. Cambiar clave
    5. Salir"""
   

def estado_puerta(estado: bool) -> str:
    """Función que devuelve si la puerta está abierta o cerrada."""
    if estado == True:
        return "La puerta está abierta."
    else:
        return "La puerta está cerrada."

def abrir_puerta(estado: bool, clave: str, clave_correcta: str) -> str:
    """Función que abre la puerta si la clave es correcta."""
    if estado == False:
        if clave == clave_correcta:
            return "La puerta se ha abierto."
        else:
            return "Clave incorrecta. La puerta no se ha abierto."
    else:
        return "La puerta ya está abierta."
    
def cerrar_puerta(estado: bool) -> str:
    """Función que cierra la puerta."""
    if estado == True:
        return "La puerta se ha cerrado."
    else:
        return "La puerta ya está cerrada."

def cambiar_clave(clave: str, clave_correcta: str) -> bool:
    """Función que cambia la clave si la clave actual es correcta."""
    if clave == clave_correcta:
        return True
    else:
        return False
    