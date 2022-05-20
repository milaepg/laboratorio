# -*- coding: cp1252 -*- 
# Calcula el n�mero aproximado de �tomos de una persona y el 
# porcentaje del universo que ellos representan

# CONSTANTES
ATOMOS_UNIVERSO = 10 ** 81
PESO_PROMEDIO = 70
ATOMOS_PROMEDIO = 7 * 10 ** 27
# ENTRADAS
# Se solicita el peso de la persona
peso = float(input("Ingrese su peso en kilogramos: "))

# PROCESAMIENTO
# Calcula el n�mero de �tomos en la persona
numero_de_atomos = (peso / PESO_PROMEDIO) * ATOMOS_PROMEDIO
# Calcula el porcentaje de �tomos en el universo
porcentaje_atomos = (numero_de_atomos / ATOMOS_UNIVERSO) * 100

# SALIDAS
print("El n�mero de �tomos en su cuerpo es:", numero_de_atomos)
print("Sus �tomos son un", porcentaje_atomos, "% del universo") 



