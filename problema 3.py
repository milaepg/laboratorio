# -*- coding: cp1252 -*-
# Programa que calcula la hipotenusa de un tri�ngulo rect�ngulo dados sus catetos
# ENTRADAS
cateto_uno = float(input("Ingrese el valor de un cateto: "))
cateto_dos = float(input("Ingrese el valor del otro cateto: "))

# PROCESAMIENTO
hipotenusa = (cateto_uno ** 2 + cateto_dos ** 2) ** 0.5
 
# SALIDAS
print("El valor de la hipotenusa del tri�ngulo rect�ngulo con catetos",
      cateto_uno, "y", cateto_dos, "es:",hipotenusa) 
