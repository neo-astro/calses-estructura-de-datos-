# Una escuela aplica dos exámenes a sus aspirantes, por lo que cada uno de ellos obtiene dos calificaciones
# denotadas como C1 y C2.
# El aspirante que obtenga calificaciones mayores que 80 en ambos exámenes es aceptado; en caso contrario es rechazado.
class Notas:

    def run(self):

        try:
            c1 = float(input("Ingrese la primera nota:"))
            c2 = float(input("Ingrese la primera nota:"))
            if c1 > 0 and c2 > 0:
                if c1 > 80 and c2 > 80:
                    print("Aceptado")
                else:
                    print("Rechazado")
            else:
                return Notas.run(self)
        except ValueError:
            print("Dato incorrecto, ingrese nuevamente los datos")
            return Notas.run(self)


hacer = Notas()
hacer.run()