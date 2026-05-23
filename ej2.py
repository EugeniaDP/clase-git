# Corregí el programa para que imprima solamente los múltiplos de 3.

numero = int(input("Ingrese un número entero: "))

for i in range(numero):
    if i % 3 == 0:
        print(i)