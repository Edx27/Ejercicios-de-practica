# Ejercicios-de-practica
# Ejercicio 1: Suma de dos números

#variables
numero1 = 20
numero2 = 5

#operaciones
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

#resultados
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)

# Ejercicio 2: Concatenación de cadenas 

# Creamos las variables de texto
nombre = "Eduardo"
apellido = "Rodriguez"

# Unimos el nombre y el apellido usando el operador +
nombre_completo = nombre + " " + apellido

# Mostramos el resultado
print("Nombre completo:", nombre_completo)

# Ejercicio 3: Módulo par o impar

# Declaramos un número
numero = 15

# Comprobamos si el resto de dividir entre 2 es 0
if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")


    # Ejercicio 4: Comparaciones lógicas

# edades
edad1 = 20
edad2 = 18

#comparaciones
son_iguales = edad1 == edad2
primera_es_mayor = edad1 > edad2
ambas_mayores_18 = edad1 > 18 and edad2 > 18

#resultados
print("¿Las edades son iguales?:", son_iguales)
print("¿La primera edad es mayor?:", primera_es_mayor)
print("¿Ambas son mayores de 18?:", ambas_mayores_18)

# Ejercicio 5: Repetir una cadena

# Repetimos el carácter "=" 40 veces
linea = "=" * 40

# Mostramos la línea
print(linea)


# Ejercicio 6: Constantes físicas

# Importamos la librería math para utilizar el valor de PI
import math

# Definimos PI en mayúsculas como indica el ejercicio
PI = math.pi

# Definimos el radio del círculo
RADIO = 5

# Calculamos el área del círculo
AREA = PI * RADIO ** 2

# Mostramos el resultado
print("PI:", PI)
print("Radio:", RADIO)
print("Área del círculo:", AREA)
