"""
Taller Final - Unidad 3
Electiva de Profundización Técnica - UNICARIBE
"""

import warnings


# ======================================================================
# EJERCICIO 1: Sistema de Control de Inventario y Precios
# Encapsulamiento y @property
# ======================================================================
class Producto:
    PRECIO_MIN = 0
    PRECIO_MAX = 10_000

    def __init__(self, nombre):
        self.__nombre = nombre
        self.__precios_historicos = []

    @property
    def nombre(self):
        return self.__nombre

    @property
    def precios_historicos(self):
        # Se devuelve una copia para proteger la lista privada
        return list(self.__precios_historicos)

    # --- Propiedad con setter validado -------------------------------
    @property
    def precio_actual(self):
        """Último precio registrado (None si no hay historial)."""
        if not self.__precios_historicos:
            return None
        return self.__precios_historicos[-1]

    @precio_actual.setter
    def precio_actual(self, nuevo_precio):
        if not isinstance(nuevo_precio, (int, float)) or isinstance(nuevo_precio, bool):
            warnings.warn("Advertencia: el precio debe ser un número. Registro sin cambios.")
            return
        if nuevo_precio < self.PRECIO_MIN or nuevo_precio > self.PRECIO_MAX:
            warnings.warn(
                f"Advertencia: precio {nuevo_precio} fuera del rango permitido "
                f"({self.PRECIO_MIN} - {self.PRECIO_MAX}). Registro sin cambios."
            )
            return
        self.__precios_historicos.append(nuevo_precio)

    # --- Método para registrar un nuevo precio -----------------------
    def registrar_precio(self, precio):
        self.precio_actual = precio  # pasa por el setter con validación

    # --- Precio promedio ---------------------------------------------
    @property
    def precio_promedio(self):
        if not self.__precios_historicos:
            return 0
        return sum(self.__precios_historicos) / len(self.__precios_historicos)

    def __str__(self):
        return (f"Producto: {self.__nombre} | Precios: {self.__precios_historicos} "
                f"| Promedio: {self.precio_promedio:.2f}")


# ======================================================================
# EJERCICIO 2: Sistema de Cotización de Envíos
# Herencia y Polimorfismo
# ======================================================================
class Envio:
    def __init__(self, peso_kg, distancia_km):
        self.peso_kg = peso_kg
        self.distancia_km = distancia_km

    def calcular_costo(self, monto_base):
        # Método a sobrescribir en las subclases
        raise NotImplementedError("Las subclases deben implementar calcular_costo")


class EnvioEstandar(Envio):
    RECARGO = 0.05

    def calcular_costo(self, monto_base):
        return monto_base * (1 + self.RECARGO)


class EnvioExpress(Envio):
    RECARGO = 0.15

    def calcular_costo(self, monto_base):
        return monto_base * (1 + self.RECARGO)


# ======================================================================
# PRUEBAS
# ======================================================================
if __name__ == "__main__":
    print("=== EJERCICIO 1: Producto ===")
    p = Producto("Cuaderno")
    p.registrar_precio(2500)
    p.registrar_precio(3000)
    p.precio_actual = 3500          # uso directo del setter
    p.registrar_precio(-50)         # inválido: negativo
    p.registrar_precio(15000)       # inválido: mayor a 10.000
    print(p)
    print(f"Precio actual: {p.precio_actual}")
    print(f"Precio promedio: {p.precio_promedio:.2f}")

    print("\n=== EJERCICIO 2: Envíos ===")
    envios = [
        EnvioEstandar(peso_kg=5, distancia_km=120),
        EnvioExpress(peso_kg=2, distancia_km=300),
        EnvioEstandar(peso_kg=10, distancia_km=50),
        EnvioExpress(peso_kg=7, distancia_km=80),
    ]
    monto_base = 100_000
    for e in envios:
        costo = e.calcular_costo(monto_base)
        print(f"{type(e).__name__:<14} | {e.peso_kg} kg | {e.distancia_km} km "
              f"| Monto base: ${monto_base:,.0f} -> Costo: ${costo:,.0f}")
