
from control_temperatura.registro import (pedir_temperatura, 
                                         mostrar_temperatura)

from control_temperatura.verificacion import mostrar_estado

for i in range(3):
    temperatura = pedir_temperatura()
    mostrar_temperatura(temperatura)
    mostrar_estado(temperatura)