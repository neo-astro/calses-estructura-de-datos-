def main():

    ht = int(input("Escriba la cantidad de horas trabajdas: "))

    if ht <  and ht == str:
        return print("Dato incorrecto!"), main()

    ph = int(input("Escriba el valor a pagar por hora: "))


    if ht <= 40 > 0:
        print("El total a pagar es :{}".format(ph * ht))

    elif 40 < ht <= 48:
        he1 = ph*40 + ((ht - 40)*(2*ph))
        print("El total a pagar es :{}".format(he1))

    elif ht > 48:
        he2 = (ph*40) + 8*(2*ph) + (ht - 48)*(3*ph)
        print("El total a pagar es :{}".format(he2))


if __name__ == '__main__':
    main()