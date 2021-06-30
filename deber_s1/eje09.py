# Calcular la suma de los cuadrados de los primeros 100 enteros y escribir el resultado.
class Suma_cuadrados:
    def run(self):
        suma = 0
        for i in range(101):
            suma += i*i
        print("La suma de los cuadrados de los primeros 100 enteros es:{}".format(suma))


ejecutar = Suma_cuadrados()
ejecutar.run()
