cliente1= {"Nombre":"Julio","Apellido": "Funes"}
cliente2= {"Nombre": "Jimena", "Apellido": "Lourdes"}

class Persona:
    def __init__(self, persona:dict):
        self.nombre = persona.get("nombre")
        self.apellido = persona.get("apellido")

    def __init__ (self, nombre ="", apellido = ""):
        self.nombre = nombre
        self.apellido = apellido
    def __repr__(self):
        return f"->Persona:[nombre]={self.nombre}, [apellido]= {self.apellido}"
if __name__=="__main__":
    p1= Persona(cliente1)       #Objeto= Persona(cliente1)
    p2= Persona(cliente2)       #p1/p2 es una referencia al objeto
    print(p1)
    print(p2)
    p3=p1
    p3.nombre="Jorgito"
    print(p1)
     
    