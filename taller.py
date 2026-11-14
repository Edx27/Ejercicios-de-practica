

Soluciones a los Ejercicios Propuestos 1 y 2

class Estudiante:
    NOTA_MIN = 0.0
    NOTA_MAX = 5.0

    def __init__(self, nombre: str):
        self.__nombre = nombre      # Atributo privado
        self.__notas = []           # Atributo privado (lista)

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def notas(self) -> list:
        # Retorna una copia para evitar mutabilidad no deseada desde afuera
        return self.__notas.copy()

    def agregar_nota(self, nota: float) -> None:
        # Validación: no se permiten valores negativos ni superiores a 5.0
        if self.NOTA_MIN <= nota <= self.NOTA_MAX:
            self.__notas.append(nota)
        else:
            raise ValueError(
                f"Nota inválida ({nota}). Debe estar entre "
                f"{self.NOTA_MIN} y {self.NOTA_MAX}."
            )

    def calcular_promedio(self) -> float:
        if not self.__notas:
            return 0.0
        return sum(self.__notas) / len(self.__notas)



# EJERCICIO PROPUESTO 2: Simulador de Tarjetas de Crédito

class TarjetaCredito:
    def __init__(self, titular: str):
        self.titular = titular

    def calcular_cashback(self, monto: float) -> float:
        return 0.0                  # Base: sin cashback


class TarjetaGold(TarjetaCredito):
    def calcular_cashback(self, monto: float) -> float:
        return monto * 0.02         # 2 %


class TarjetaBlack(TarjetaCredito):
    def calcular_cashback(self, monto: float) -> float:
        return monto * 0.05         # 5 %



if __name__ == "__main__":
    print("=== Ejercicio 1 ===")
    est = Estudiante("Laura Pérez")
    for n in (4.5, 3.8, 5.0):
        est.agregar_nota(n)
    print("Notas:", est.notas)
    print(f"Promedio: {est.calcular_promedio():.2f}")

    for invalida in (-1, 5.5):
        try:
            est.agregar_nota(invalida)
        except ValueError as e:
            print("Error:", e)

    est.notas.append(1.0)           # Modifica solo la copia
    print("Notas tras intento externo:", est.notas)

    print("\n=== Ejercicio 2 ===")
    tarjetas = [TarjetaCredito("Ana"), TarjetaGold("Luis"), TarjetaBlack("Marta")]
    compra = 1000.0
    for t in tarjetas:              # Invocación polimórfica
        print(f"{type(t).__name__:15} -> cashback: ${t.calcular_cashback(compra):.2f}")
