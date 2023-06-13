class Persona:  
    def __init__(self, param_nombre, param_email):
        self.nombre = param_nombre
        self.email = param_email
        self.asistencia = 0
    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def asistencia_clase(self):
        self.asistencia += 1

class Profesor(Persona):
    def __init__(self, param_nombre, param_email, legajo_empleado):
        self.legajo_empleado = legajo_empleado
        super().__init__(param_nombre, param_email)

    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def asistecia_clase(self):
        self.asistencia += 1

class Alumno(Persona):
    def __init__(self, param_nombre, param_email, numero_alumno):
        self.numero_alumno = numero_alumno
        self.materias_cursando = []
        super().__init__(param_nombre, param_email)
    def cursando(self, materia):
        self.materias_cursando.append(materia)


profesor_Franco = Profesor("Franco", "f.pasqual@um.edu.ar", "62199")
print(id(profesor_Franco))
print(profesor_Franco.nombre)
profesor_Franco.cambiar_nombre("Pasqui")

print("el nombre es: ")
print(profesor_Franco.nombre)
print("el email es: ")
print(profesor_Franco.email)
print("Legajo: ")
print(profesor_Franco.legajo_empleado)

profesor_Franco.asistecia_clase()
profesor_Franco.asistecia_clase()
profesor_Franco.asistecia_clase()

print("su asistencia es: ")
print(profesor_Franco.asistencia)

print("el profesor fue a clase...")


print("     ")


profesor_Quinteros = Profesor("Joaco", "joaquetin@um.ar", "62134")
print(id(profesor_Quinteros))
print(profesor_Quinteros.nombre)

print("el nombre es: ")
print(profesor_Quinteros.nombre)
print("el email es: ")
print(profesor_Quinteros.email)
print("Legajo: ")
print(profesor_Quinteros.legajo_empleado)

print("el profesor fue a clase...")
profesor_Quinteros.asistecia_clase()
profesor_Quinteros.asistecia_clase()

print("su asistencia es: ")
print(profesor_Quinteros.asistencia)



print("   ")



profesor_Tellez = Profesor("Niko", "kiki@alum.ar", "62187")
print(id(profesor_Tellez))
print(profesor_Tellez.nombre)

print("el nombre es: ")
print(profesor_Tellez.nombre)
print("el email es: ")
print(profesor_Tellez.email)
print("Legajo: ")
print(profesor_Tellez.legajo_empleado)

print("el profesor fue a clase...")
profesor_Tellez.asistecia_clase()
profesor_Tellez.asistecia_clase()

print("su asistencia es: ")
print(profesor_Tellez.asistencia)

