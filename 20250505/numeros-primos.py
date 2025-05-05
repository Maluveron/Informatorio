# Ejercicio: Definir una lista de 1..1000 y determinen todos los numeros primos que aparecen
# entre el 1 y el 1000, y guardarlos en una lista llamada numeros_primos.

# Resolucion:

numeros = list(range(1, 1001))
numer_primos = []

for numero in numeros:
    if numero > 1: # Los numeros menores o iguales a 1 no son primos
        es_primo = True
        for i in range(2, int()