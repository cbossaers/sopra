class Ejercicio1:
    def obtenerTipo(num):
        if(num % 2 == 0): return "par"
        else: return "impar"

    def leerNumero():
        NUMERO = int(input("Introduce un número: "))
        if(NUMERO < 0):
            raise ValueError("El número debe ser positivo")
        return NUMERO

    def main():
        try:
            numero = Ejercicio1.leerNumero()
        except ValueError as e:
            print(f"Error: {e.args[0]}")
            Ejercicio1.main()

        tipo = Ejercicio1.obtenerTipo(numero)

        print(f"El número introducido ({numero}) es {tipo}\n")
        print("La secuencia es la siguiente: ")

        aux = numero

        while(aux >= 0):
            print(aux)
            aux = aux - 2

Ejercicio1.main()