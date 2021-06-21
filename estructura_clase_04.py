class FOR:

    def __init__(self):
        pass

    def usofor(self):
        # nombre =  "Adrian"
        # datos = ["Daniel", "Se" ,True ]
        # numeros = (2, 5.6, 4 ,1)
        # docente = {"nombre":"Daniel","edad":50 , "fac":"faci"}
        # listaNotas = [(30,40),(20,40,50),(50,40)]
        # listaAlumnos = [{"nombre":"Erick","Final":70,},{"nombre":"Yady","final":60},{"nombre":"Dadi","final":90}]

        # j = 0
        # while j<5 :
        #     print('while' , j)
        #     j +=j

        # for i in range (5):
        #     print("for",i,end="")
        # print()

        # for i in range (1,5,end=""):
        #     print("for",i)
        # print()

        # for i in range (2,10,2,end=""):
        #     print("for",i)
        # print()

        # for i in range (12,3,-3,end=""):
        #      print("for",i)
        # print()

        # lon = len(nombre)
        # for pos in range (lon):
        #     if pos%2 == 0 and pos !=0:
        #         print(pos, nombre[pos])

        # for elem in nombre:
        #     print(elem,end=" ")
        #     nombre

        # lon = len(datos)
        # for pos in range(lon):
        #     print(pos,datos[pos])

        # for pos,valor in enumerate(datos):
        #     print(pos,valor)

        # for clave,valor in docente.items():
        #     print(clave,valor,end= " ")

        # print(listaNotas)
        # for notas in listaNotas:
        #     for nota in notas:
        #         print(nota, end=" ")
        #     print("saliendo del for interno")

        # print(listaNotas)
        # for notas in listaNotas:
        #     acum = 0
        #     for nota in notas:
        #         acum += nota
        #     print(acum/len(notas), end=" ")

        # print ("/nDICCIONARIO DE NOTAS")
        # for alumnos in listaAlumnos:
        #     print(alumnos)
        #     for clave,valor in alumnos.items():
        #         print(clave , ":",valor ,end = " ")
        #     print()

        listaAlumnos = [{"nombre":"ADRIAN", "final":70},{"nombre":"Yandel","final":"60"}]
        print("/nDiccionario de alumnos")
        print(listaAlumnos)
        acum = 0
        for alumnos in listaAlumnos:
            print(alumnos)
            for clave,valor in alumnos.items():
                print(clave, ":",end=" ")
                # if type(valor) == "final":
                if clave == "final":
                   acum += valor
        print("Promedio",acum/len(listaAlumnos))
        
        listaNotas = [(14,25),(10,30,20),(30,50)]
        acum,cont = 0,0
        
        for notas in listaNotas:
            print(notas)
            acum_parcial = 0
            
            for nota in notas:
                acum_parcial += nota
            cont += len(notas) 
            acum = acum +acum_parcial
            print("Total Parcial :{} Promedio parcial: {}".format(acum_parcial,acum_parcial/len(notas)))
        
        print("Total Gneral : {} Promedio : {}".format(acum,acum/cont))
        
bucle = FOR()
bucle.usofor()
