# -*- coding: cp1252 -*-
# Programa que convierte d�as a segundos
# CONSTANTES
HORAS_DIA = 24
SEGUNDOS_HORA = 3600

# DATOS DE ENTRADA 
# Se solicita el n�mero de d�as a convertir
dias = int(input("Ingrese el n�mero de d�as: "))

# PROCESAMIENTO
# Calcular el total de segundos 
segundos = dias * HORAS_DIA * SEGUNDOS_HORA

# SALIDA
# Entrega el total de segundos
print(dias, "d�as equivalen a:", segundos, "segundos.") 
