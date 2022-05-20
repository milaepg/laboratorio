#Calcula el número de total de granos solicitados por Sissa y
#el porcentaje que representa respecto a la producción mundial de trigo

# CONSTANTES
GRANOS_KILO = 22000
KILOS_TONELADA = 1000
PRODUCCION_MUNDIAL = 763000000

# PROCESAMIENTO
# Calcula el total de trigo en toneladas
trigo_total = (((2 ** 64 - 1) / GRANOS_KILO) / KILOS_TONELADA)
# Calcula el procentaje respecto a la producción mundial
porcentaje = (trigo_total / PRODUCCION_MUNDIAL) * 100

# SALIDAS
print('El total de granos solicitados por Sissa es: ', trigo_total, 'toneladas')
print('Porcentaje que representa respecto a la producción mundial es: ', porcentaje, '%')
