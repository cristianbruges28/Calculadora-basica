print("Calculadora")

valor1 = float(input("Digite el primer número: "))
valor2 = float(input("Digite el segundo número: "))

print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

seleccion = input("Seleccione una opción: ")

if seleccion == "1":
print("Resultado:", valor1 + valor2)

elif seleccion == "2":
print("Resultado:", valor1 - valor2)

elif seleccion == "3":
print("Resultado:", valor1 * valor2)

elif seleccion == "4":
if valor2 != 0:
print("Resultado:", valor1 / valor2)
else:
print("No se puede dividir entre cero")

else:
print("Opción no válida")
