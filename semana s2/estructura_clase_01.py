num = 40
nombre ="AnITA"
print(num,type(num))
print(nombre,type(nombre))


def mensaje():
    print("hola es mi primer programa")


def mensaje2():
    print("hola es mi segundo programa")


mensaje()
mensaje2()


def mensaje(msg):
    print(msg)


mensaje("Hola aprendiendo cosas nuevas")
mensaje("Hello ")


class Sintaxis:
    instancia = 0
    
    
    def __init__(self, dato="Adrian Abril"):
        self.frase = dato
        Sintaxis.instancia = Sintaxis.instancia + 10
        
    
    def usovariable(self):
        edad = 50, 70.5
        nombre = "Daniel Vera"
        tipo_de_sexo = "Masculino"
        civil = False
        #tupla = () son colecciones de datos de cualquier tipo inmutable
        usuario = ()
        usuario = ('dchiki','1234','chiki@gmail.com')
        #ususario[3] = "milagro"
        #lista = [] colecciones mutables
        materias = ["GIT-HUB","Programacion web", "PHP","POO"]
        materias[1]="Python"
        materias.append("LETS GO")
        #diccionario = {} colecciones de objetos  clave valor tipo json 
        docente = {}
        docente = {'nombre': 'Adrian', 'eda':'23','color':'blanco'}
        edad = docente["edad"]
        docente["edad"] = "51"
        docente["Carrera"]= "ING CIVIL"
        print(usuario, usuario[2:],usuario[:3],usuario[-1])
        print(nombre, nombre[0], nombre[:2], nombre[-1])
        print (materias, materias[2:],materias[:3],materias[::-1],materias[-2:])
        #presentacion con format
        
        print("""Hola mi nombre es {} este es un triple comilla
      para separa el txt entre las lineaa , tengo {} """.format(nombre, edad[1]))

print("Sintaxis antes de la instancia = {}".format(Sintaxis.instancia))
ejer1 = Sintaxis()
print("Valor de Sintaxis despues de la instacia {}".format(ejer1.instancia))
ejer2 = Sintaxis("Cambiando el parametro")
print(ejer1.frase)
print("Sintaxis de ejer2 es: {} ".format(Sintaxis.instancia))
print("Otra vez Sintaxis de ejer2 es: {} ".format(Sintaxis.instancia))
print(ejer2.frase)
print("Valor de instacia nuevamente = {}".format(Sintaxis.instancia))
