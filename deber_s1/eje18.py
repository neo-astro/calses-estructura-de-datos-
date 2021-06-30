
def run():
    try:
        import random

        promedio1, promedio2, promedio3, promedio4, promedio5, promedio6 = 0, 0, 0, 0, 0, 0
        a = []
        b = []
        alumno = 0
        print("NOTAS DE MATERIAS".center(50, "^"), "\n           EX1 EX2 EX3 EX4 EX5 EX6\n           |  |  |  |  |  |")

        while len(a) != 30:

            for i in range(6):
                b.append(random.randint(0, 10))

            a.append(b)
            print("Alumno {}:".format(alumno + 1), b, " ; Promedio de notas = {}".format(round(sum(b) / 6, 3)), "\n")
            alumno += 1
            promedio1 += b[0]
            promedio2 += b[1]
            promedio3 += b[2]
            promedio4 += b[3]
            promedio5 += b[4]
            promedio6 += b[5]
            b = []

        print("""
        El promedio del ex1 ={} 
        El promedio del ex2 ={} 
        El promedio del ex3 ={} 
        El promedio del ex4 ={} 
        El promedio del ex5 ={} 
        El promedio del ex6 ={} 
        """.format(round((promedio1 / 30), 3), round((promedio2 / 30), 3), round((promedio3 / 30), 3),
                   round((promedio4 / 30), 3), round((promedio6 / 30), 3), round((promedio6 / 30), 3)))
    except ValueError:
        return print("Dato incorrecto , intentalo nuevamente"), run()

if __name__ == '__main__':
    run()