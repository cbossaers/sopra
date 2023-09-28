
class Ejercicio3:
    def obtenerDatos():
        tarifa = float(input(f"Por favor introduzca el salario por horas: "))
        horas = int(input(f"Por favor, introduzca el número de horas trabajadas: "))

        return tarifa, horas

    def procesarSalario(tarifa, horas):
        horasExtra = 0

        if(horas > 40): 
            horasExtra = horas - 40
            horas = 40

        salario = (horas * tarifa) + (horasExtra * (tarifa * 1.5))
        
        return salario

    def main():
        try:
            tarifa, horas = Ejercicio3.obtenerDatos()

            salario = Ejercicio3.procesarSalario(tarifa, horas)
            print(f"El salario correspondiente a {horas} horas con una tarifa de {tarifa}€/hora es de {salario}€")
        except ValueError as e:
            print(f"Error: {e.args[0]}")
            Ejercicio3.main()


Ejercicio3.main()
