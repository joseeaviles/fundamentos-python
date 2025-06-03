'''
Clase:        Clase 7
Tema:         Introducción a NumPy 
Ejercicio:    Cuestionario
Descripción:  completar cuestionario en base el array

Autor:        Jose Andres Aviles Torres 
Fecha:        2025-05-30
Estado:       [ Terminado ]
'''


import numpy as np

""" Reporte de consumo energético semanal """

# Matriz de consumo (hogares x días)
datos_consumo = np.array([
    [12.5, 13.2, 11.9, 14.0, 13.5, 15.0, 14.3],
    [10.1, 10.5, 10.0, 11.2, 11.5, 12.0, 11.8],
    [14.0, 14.2, 13.9, 15.5, 15.1, 16.0, 15.8],
    [9.0, 9.2, 8.9, 9.5, 9.8, 10.0, 9.7],
    [16.2, 16.5, 16.0, 17.1, 17.4, 18.0, 17.8],
    [11.0, 11.3, 11.1, 12.0, 12.4, 12.8, 12.5],
    [13.5, 13.8, 13.2, 14.1, 14.6, 15.0, 14.9],
    [10.8, 11.0, 10.6, 11.5, 11.8, 12.2, 12.0],
    [15.1, 15.5, 15.0, 16.0, 16.4, 17.0, 16.7],
    [8.5, 8.7, 8.4, 9.0, 9.2, 9.5, 9.3],
])

# 1. Consumo del hogar número 5 el viernes
consumo_viernes_h5 = datos_consumo[4, 4]
print(f"Consumo del hogar 5 el viernes: {consumo_viernes_h5}")

# 2. Consumo de los últimos 3 hogares el domingo
consumo_domingo_ult3 = datos_consumo[-3:, 6]
print(f"Consumo de los últimos 3 hogares el domingo: {consumo_domingo_ult3}")

# 3. Promedio de consumo por hogar durante sábado y domingo
prom_finde_semana = np.mean(datos_consumo[:, 5:], axis=1)
print(f"Promedio de consumo en fines de semana por hogar: {prom_finde_semana}")

# 4. Día de la semana con mayor dispersión entre hogares
desv_por_dia = np.std(datos_consumo, axis=0)
dia_mas_variable = np.argmax(desv_por_dia)
print(f"Día con mayor desviación estándar: Día {dia_mas_variable} (0=Lunes)")

# 5. Los 3 hogares con menor consumo acumulado en la semana
total_por_hogar = np.sum(datos_consumo, axis=1)
menores_consumos_idx = np.argsort(total_por_hogar)[:3]
menores_consumos_val = total_por_hogar[menores_consumos_idx]
print(f"Hogares con menor consumo total: {menores_consumos_idx}")
print(f"Valores de consumo total: {menores_consumos_val}")

# 6. Nuevo consumo semanal del hogar 3 con un aumento del 10% diario
incremento_h3 = datos_consumo[2] * 1.10
nuevo_total_h3 = np.sum(incremento_h3)
print(f"Nuevo total semanal del hogar 3 con aumento del 10%: {nuevo_total_h3}")