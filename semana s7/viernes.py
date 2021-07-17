class Ejercicios():

    def __init__(self,datos):
        self.lista = datos



    def parimpar(self, num):
        if num % 2 == 0:
            print("El numero {} es par".format(num))
        else:
            print("El numero {} no es par".format(num))
    def perfecto(self,num):
        acum = 0
        for numero in range(1,num):
            if num % numero == 0:
                acum += numero
        if acum == num:
            print(f"El numero {num} es perfecto!")
        else:
            print(f"El numero {num} no tiene perfecto!")

    def perfecto2(self,num):
        acum = 0
        for numero in range(1,num):
            if num % numero == 0:
                acum += numero
        return acum


class Programacion(Ejercicios):
    
    def __init__(self,valor):
        super().__init__(valor)
        self.dato =valor
            
    # def divisores(self,num):
    #     cont =1
    #     divisores = []
    #     while cont < num:
    #         rec =num% cont
    #         if rec ==0:
    #             divisores.append(cont)
    #         cont = cont + 1
    #     print(divisores)


    def divisores(self,num):
        divisores = []
        for cont in range(1,num):
            rec = num %cont
            if rec == 0:
                divisores.append(cont)
        return divisores



pro1 = Programacion(20)
print(pro1.divisores(4))
print(pro1.lista)

# div = pro1.divisores(6)
# lista = [1,2]
# lista2 = lista + div
# print(lista2)
# pro1




