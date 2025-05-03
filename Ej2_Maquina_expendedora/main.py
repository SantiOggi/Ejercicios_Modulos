from maquina import (menu, 
                    verificar_producto,
                    precio, 
                    verificar_dinero,
                    vuelto,
                    faltante)

menu()

producto_elegido = (input("Seleccione el producto: ")).lower()
while not verificar_producto(producto_elegido):
        print("Producto no válido, seleccione nuevamente")
        producto_elegido = (input("Seleccione el producto: ")).lower()

dinero_necesario = precio(producto_elegido)
print(f"El precio del producto es: {dinero_necesario}")

dinero = int(input("Ingrese con cuánto dinero paga: "))
while dinero < 0:
    print("El dinero no puede ser negativo, por favor ingrese nuevamente")
    dinero = int(input("Ingrese con cuánto dinero paga: "))

alcanza= verificar_dinero(dinero, dinero_necesario)
while not alcanza:
    faltante_total = faltante(dinero, dinero_necesario)
    print(f"Dinero insuficiente, faltan ${faltante_total}, por favor ingrese más dinero")
    dinero = int(input("Ingrese con cuánto dinero paga: "))
    alcanza= verificar_dinero(dinero, dinero_necesario) 
   
print("Compra exitosa")
vuelto_total = vuelto(dinero, dinero_necesario)
if vuelto_total == 0:
    print("Pago exacto")
else:
    print(f"Su vuelto es: ${vuelto_total}")
print("Gracias por su compra, vuelva prontos.")

