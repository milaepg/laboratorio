# -*- coding: cp1252 -*-
# Calcula el �rea de un tri�ngulo mediante la f�rmula de Her�n
# ENTRADAS
# Se solicita el ingreso de los lados
a = float(input("ingrese el valor de uno de los lados del tri�ngulo: "))
b = float(input("ingrese el valor de otro de los lados: "))
c = float(input("ingrese el valor del lado restante: "))

# PROCESAMIENTO 
# Calcula el semiper�metro
semi = (a + b + c) / 2
# Calcula el �rea
area = (semi * (semi - a) * (semi - b) * (semi - c)) ** 0.5

# SALIDAS
# Entrega el �rea y los lados
print("El valor del �rea del tri�ngulo de lados", a, b, c, "es :", area) 

