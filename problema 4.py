# -*- coding: cp1252 -*-
# Calcula el área de un triángulo mediante la fórmula de Herón
# ENTRADAS
# Se solicita el ingreso de los lados
a = float(input("ingrese el valor de uno de los lados del triángulo: "))
b = float(input("ingrese el valor de otro de los lados: "))
c = float(input("ingrese el valor del lado restante: "))

# PROCESAMIENTO 
# Calcula el semiperímetro
semi = (a + b + c) / 2
# Calcula el área
area = (semi * (semi - a) * (semi - b) * (semi - c)) ** 0.5

# SALIDAS
# Entrega el área y los lados
print("El valor del área del triángulo de lados", a, b, c, "es :", area) 

