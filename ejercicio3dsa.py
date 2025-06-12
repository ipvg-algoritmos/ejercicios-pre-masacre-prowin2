numeros = []

numero = float(input("Ingrese un número (negativo para terminar): "))

while numero >= 0:
    numeros.append(numero)
    numero = float(input("Ingrese un número (negativo para terminar): "))

if not numeros:
    print("No se ingresaron números válidos.")
else:
    mayor = max(numeros)
    menor = min(numeros)
    print(f"Número mayor: {mayor}")
    print(f"Número menor: {menor}")



















