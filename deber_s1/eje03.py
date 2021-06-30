# Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas.
# El vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por las tres
# ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y sus comisiones.

def pago():
    try:
        sueldo = float(input("Escriba el sueldo base del empleado: "))
        comi1 = float(input("Escriba el valor de la venta 1: "))
        comi2 = float(input("Escriba el valor de la venta 2: "))
        comi3 = float(input("Escriba el valor de la venta 3: "))
        r = sueldo + (comi3 + comi1 + comi2)*0.1
        print("EL TOTAL A PAGAR AL EMPLEADO ES DE : {} $ , comisiones = {} $".format(r, (comi2+comi3+comi1)*0.1))


    except ValueError:
        return print(("DATO INCORRECTO, INTENTALO NUEVAMENTE").center(50, "-")), pago()
if __name__ == '__main__':
    pago()