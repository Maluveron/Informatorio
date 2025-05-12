# Ejercicio: Definir una lista de 1..1000 y determinen todos los numeros primos que aparecen
# entre el 1 y el 1000, y guardarlos en una lista llamada numeros_primos.

# Resolucion:


numeros = list(range(1, 1001))
numer_primos = []

for numero in numeros:
    if numero > 1: # Los numeros menores o iguales a 1 no son primos
        es_primo = True
        for i in range(2, int(numero ** 0.5) + 1): # Solo se verifica hasta la raiz cuadrada del numero
            # Si el numero es divisible por i, no es primo
            if numero % i == 0:
                es_primo = False
                break
        if es_primo:
            numer_primos.append(numero)
print("Los numeros primos entre 1 y 1000 son:")
for primo in numer_primos:
    print(primo, end=", ")
print("\nTotal de numeros primos:", len(numer_primos))

