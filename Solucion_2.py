"""Usando el concepto de herencia y encapsulación (para saldo) para crear
el siguiente programa (3 ptos):
Reglas:
- Agregar un atributo saldo a la clase persona (ejercicio anterior).
- Crear un método transferencia y mostrar saldo (mostrará el saldo actual
que tiene la persona) para la clase mencionada
- El método transferencia hace que la Persona que llame al método pueda
transferir la cantidad monto al objeto Persona2 por consiguiente deberá
ir actualizando también el saldo o monto que tiene la otra persona en su
cuenta cada vez que use el método transferencia

- Comprobar si no se tiene dinero suficiente no se ejecuta la acción e
imprimir “Saldo insuficiente”. Comprobar instanciado la clase por lo
menos realizando una transferencia y con dos personas."""

from Solucion_1 import Persona
class Empleado(Persona):
    pass
    def __init__(self, nombre, edad, saldo):
        super().__init__(nombre, edad, saldo)
        self.__saldo = saldo
        self.nacionalidad = "peruana"

    #Getters
    def getSaldo(self):
        return self.__saldo

    #Setters
    def setSaldo(self, saldo):
        if saldo <= 0:
            print("El saldo no puede ser negativo o igual a 0")
        else:
            self.__saldo = saldo

    def transferir(self, monto, personaDestino):
        if self.__saldo < monto:
            print("Saldo insuficiente")
        else:
            self.__saldo -= monto
            personaDestino.__saldo += monto
            print("El monto especificado ha sido transferido exitosamente")
def main():
    e1 = Empleado("Juan Perez",20,0)
    e2 = Empleado("Benito Juarez",19,0)

    e1.setSaldo(3000)
    e2.setSaldo(4000)

    print(f"Saldo inicial de {e1.nombre}: {e1.getSaldo()}")
    print(f"Saldo inicial de {e2.nombre}: {e2.getSaldo()}")

    e1.transferir(500, e2)

    print(f"Saldo final de {e1.nombre}: {e1.getSaldo()}")
    print(f"Saldo final de {e2.nombre}: {e2.getSaldo()}")

    e1. transferir(231890, e2)
    
if __name__ == "__main__":
    main()