import random
from personaClass import Persona

class Ejercicio2:
    
    personas = []
    cantidad = 50

    #Se crean <cantidad> objetos Persona y se añaden al array personas
    def cargarPersonas():
        for i in range(Ejercicio2.cantidad):
            #0 Hombre, 1 Mujer
            sexo = random.randint(0,1)
            edad = random.randint(0,99)

            Ejercicio2.personas.append(Persona(sexo, edad))

    def mayoresDeEdad():
        contador = 0

        for persona in Ejercicio2.personas:
            if persona.edad >= 18: contador += 1
        
        return contador
    
    def menoresDeEdad():
        contador = 0

        for persona in Ejercicio2.personas:
            if persona.edad < 18: contador += 1
        
        return contador
    
    def masculinasMayores():
        contador = 0

        for persona in Ejercicio2.personas:
            if persona.edad >= 18 and persona.sexo == 0: 
                contador += 1
        
        return contador
    
    def femeninasMenores():
        contador = 0

        for persona in Ejercicio2.personas:
            if persona.edad < 18 and persona.sexo == 1: 
                contador += 1
        
        return contador
    
    def porcentajeMayores():
        mayores = Ejercicio2.mayoresDeEdad()

        porcentaje = int(100*mayores/Ejercicio2.cantidad)
        return porcentaje
    
    def porcentajeMujeres():
        contador = 0

        for persona in Ejercicio2.personas:
            if persona.sexo == 1: 
                contador += 1
        
        porcentaje = int(100*contador/Ejercicio2.cantidad)
        return porcentaje
    
    def main():
        Ejercicio2.cargarPersonas()

        print(f"Existen {Ejercicio2.mayoresDeEdad()} cantidad de personas mayores de edad")
        print(f"Existen {Ejercicio2.menoresDeEdad()} cantidad de personas menores de edad")
        print(f"Existen {Ejercicio2.masculinasMayores()} cantidad de personas masculinas y mayores de edad")
        print(f"Existen {Ejercicio2.femeninasMenores()} cantidad de personas femeninas y menores de edad")
        print(f"Existen un porcentaje del {Ejercicio2.porcentajeMayores()}% de personas mayores de edad")
        print(f"Existe un porcentaje del {Ejercicio2.porcentajeMujeres()}% de mujeres")


Ejercicio2.main()