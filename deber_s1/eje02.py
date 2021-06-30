# En una tienda se ofrece un descuento del 15% sobre el total de la compra
# y un cliente desea saber cuánto deberá pagar finalmente por su compra.
def porcentaje():
    try:
        total = float(input("Escriba el total a pagar: "))
        res = total - total*0.15
        print("El total a pagar es de {} $".format(res))
    except ValueError:
        return print("Dato incorrecto, intentelo nuevamente"), porcentaje()

porcentaje()