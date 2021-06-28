from random import *
import numpy as np 
# En code no reconoce numpy
ma = [[randint(1, 10)for i in range(6)] for j in range(30)]
matrix = np.array(ma)

cf = 0
co =1
while cf != 30:
    print("Nota", matrix[cf:co], "El promedio del alumno {}:".format(co), round((matrix[cf:co].sum()/6),2),"\n")
    cf += 1
    co += 1