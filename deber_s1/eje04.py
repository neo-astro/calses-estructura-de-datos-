
# Dado como dato la calificación de un alumno en un examen,
# escriba “aprobado” si su calificación es mayor o igual que 7 y “Reprobado” en caso contrario
def aprobado():
    try:
        nota = float(input("Escriba la nota del alumno:"))
        if nota >=7 :
            print("APROBADO")
        else:
            print("REPROBADO")
    except ValueError:
        return print("DATO INCORRECTO"), aprobado()

if __name__ == "__main__":
    aprobado()