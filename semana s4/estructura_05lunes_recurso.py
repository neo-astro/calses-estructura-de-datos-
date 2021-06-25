# class Cargo:
#     def __init__(self):
#         self.descripcion = "Sin cargo"
#         self.codigo = 10
# #PARA HACER UN ATRIBUTO PRIVADO  (SELF.__VAR)
# cargo1 = Cargo()
# print(cargo1.codigo,cargo1.descripcion)
# #cargo2 = cargo2(1,"Docente")
# cargo2 = Cargo()
# cargo2.codigo = 10
# cargo2.descripcion= "ana"
# print(cargo2.codigo,cargo2.descripcion)
# cargo3 = Cargo()
# cargo3.descripcion = "Conserje"
# cargo3.codigo = 12
# print(cargo3.descripcion,cargo3.codigo)



class Cargo:
    secuencia = 0
    def __init__(self,des="sin cargo"):
        Cargo.secuencia +=1
        self.descripcion = des
        # self.codigo = cod
        self.codigo = Cargo.secuencia
#PARA HACER UN ATRIBUTO PRIVADO  (SELF.__VAR)

# if __name__ == "__main__":
#     cargo1 = Cargo()
#     print("Ejecutando lo import")
#     print("cargo1",cargo1.descripcion,cargo1.codigo)
#     #cargo2 = cargo2(1,"Docente")
#     cargo2 = Cargo("docente")
#     print("cargo2",cargo2.descripcion,cargo2.codigo)
#     cargo3 = Cargo("docente")
#     print("cargo3",cargo3.descripcion,cargo3.codigo)
#     print("Valor de secuencia" , Cargo.secuencia)

if __name__ == "__main__":
    cargo1 = Cargo()
    print("Ejecutando lo import")
    print("cargo1",cargo1.codigo,cargo1.descripcion)
    #cargo2 = cargo2(1,"Docente")
    cargo2 = Cargo("docente")
    print("cargo2",cargo2.codigo,cargo2.descripcion)
    cargo3 = Cargo()
    print("cargo3",cargo3.codigo,cargo3.descripcion)
    print( Cargo.secuencia)

