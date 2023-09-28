class Persona:
    def __init__(self, sexo, edad):
        self._sexo = sexo
        self._edad = edad

    @property
    def sexo(self):
        return self._sexo

    @sexo.setter
    def sexo(self, value):
        if not value:
            raise ValueError("Ha de indicarse el sexo")
        
        self._sexo = value

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, value):
        if not value:
            raise ValueError("Ha de indicarse la edad")
        
        self._edad = value