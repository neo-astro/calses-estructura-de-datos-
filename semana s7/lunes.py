class Ejercicios():
    
    def __init__(self):
        pass


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

run = Ejercicios()


# num = int(input("Ingrese un numero:"))
num = int(input("Ingrese un numero: "))
print("llamada 1")
run.parimpar(num)
input("")
lista = [4,5,6,7,8,9,10]
print("llamada 2")

for num in lista:
    run.parimpar(num)
input("")

num = int(input("Ingrese un numero: "))
print("llamada 3")


if run.perfecto2(num) == num:
    print(f"El numero {num} es perfecto!")
else:
    print(f"El numero {num} no tiene perfecto")

print("Llamada a def que imprime ")
run.perfecto(28)



# pares = [i for i in range(1, 101) if i%2 == 0]
# print (pares)

