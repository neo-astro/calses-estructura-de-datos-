from estructura_05lunes_recurso import Cargo

class Empleado:
    secuencia = 0
    def __init_subclass__(self,nom="",sue="0",car="none"):
        
        # Empleado.secuencia += 1
        self.codigo = self.generar_codigo()
        self.nombre = nom
        self.sueldo = sue
        self.cargoEmp = car
    
    def generar_codigo(self):
        Empleado.secuencia += 1
        return Empleado.secuencia
    
    def mostrar (self):
        print("codigo: {} Nombre :{} Cargo ({}):{}".format(self.codigo,self.nombre,self.cargo.codigo,self.cargo.descripcion))
        
cargo1 = Cargo("docente")
emp1 = Empleado("Daniel",100,cargo1)
emp1.mostrar()
emp2 = Empleado("Moises",50,cargo1)
emp2.mostrar()