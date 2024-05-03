"""Reglas:
- Crear una clase llamada Persona donde sus atributos deben ser nombre,
edad, saldo y de nacionalidad peruana (use el manejo de errores para el
tipo de dato) y un método para solicitar su nombre y edad.
- Tendrá un método cumpleaños donde cada vez que invoque aumentará en
un año la edad de la persona.
- Crear la instancia de la clase Persona y usar su método cumpleaños para
incrementar su edad (mínimo instanciar la clase 2 veces, mostrar por
pantalla dicha edad actualizada).
- Crear una función que retorne solamente la fecha, hora y minuto que se ha
registrado esta persona (Mostrar por pantalla este valor)"""

from datetime import datetime
class Persona:
    def __init__(self, nombre, edad, saldo):
        try:
            self.nombre = str(nombre)
            self.edad = int(edad)
            self.saldo = float(saldo)
        except Exception as e:
            print(
                f"Error: {e}. Revisa que algún dato tiene correcto tipo de dato")

        self.nacionalidad = "peruana"

    def cumple(self):
        self.edad += 1
    def datos(self):
        self.nombre = input("Ingrese su nombre completo: ")
        self.edad = int(input("Ingrese su edad: "))
        self.saldo = float(input("Ingrese su saldo: "))
    def registrar(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M")

def main():

    p1 = Persona(" ", 19, 3902.32)
    p2 = Persona(" ", 25, "mirar La luna")

    p1.datos()
    print(f"Edad anterior {p1.edad}")
    p1.cumple()
    p1.cumple()
    print(f"Edad actualizada {p1.edad}")
    print(f"Fecha de registro {p1.registrar()}")

    p2.datos()
    print(f"Edad anterior {p2.edad}")
    p2.cumple()
    p2.cumple()
    print(p2.edad)
    print(f"Edad actualizada {p2.edad}")
    print(f"Fecha de registro {p2.registrar()}")

if __name__ == "__main__":
    main()
