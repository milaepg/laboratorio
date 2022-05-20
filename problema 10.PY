# Programa que calcula el valor final de un crédito con interés
# compuesto y el valor de la cuota

# ENTRADAS
# Solicita el valor inicial del crédito
valor_inicial=  float(input("Ingrese el valor del crédito: "))
# Solicita la tasa de interés
tasa_interes = float(input("Ingrese el valor de la tasa de interés: "))
# Solicita la cantidad de cuotas
numero_cuotas = int(input("Ingrese el número de cuotas: "))

# PROCESAMIENTO
# Calcula el valor final del crédito
valor_final = int(valor_inicial * (1 + (tasa_interes / 100)) ** numero_cuotas)
# Calcula el valor de la cuota
valor_cuotas = int(valor_final / numero_cuotas)

# SALIDA
print("El valor final del crédito es: ", valor_final, "pesos")
print("El valor de cada cuota es : ", valor_cuotas, "pesos")
