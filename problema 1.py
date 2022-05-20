# -*- coding: cp1252 -*-
# Programa que convierte días a segundos
# CONSTANTES
HORAS_DIA = 24
SEGUNDOS_HORA = 3600

# DATOS DE ENTRADA 
# Se solicita el número de días a convertir
dias = int(input("Ingrese el número de días: "))

# PROCESAMIENTO
# Calcular el total de segundos 
segundos = dias * HORAS_DIA * SEGUNDOS_HORA

# SALIDA
# Entrega el total de segundos
print(dias, "días equivalen a:", segundos, "segundos.") 
