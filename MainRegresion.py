#   Codigo que implementa la regresion lineal
#   para ajustar un conjunto de datos
#
#           Autor:
#   Gilbert Alexander Mendez Cervera
#   mendezgilbert222304@outlook.com
#   Version 1.01 : 11/04/2025
import numpy as np
import matplotlib.pyplot as plt

# Datos del ejercicio
x = np.array([5, 10, 15, 20, 25])       # Carga (kN)
y = np.array([0.6, 1.2, 1.9, 2.5, 3.1]) # Elongación (mm)

# Cálculo de los coeficientes
n = len(x)
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_xy = np.sum(x * y)
sum_x2 = np.sum(x**2)

# Fórmulas de regresión lineal
b = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
a = (sum_y - b * sum_x) / n

print(f"Coeficientes de la regresión:")
print(f"a (intercepto) = {a:.4f}")
print(f"b (pendiente) = {b:.4f}")

# Predicción usando el modelo
y_pred = a + b * x

# Gráfica
plt.figure(figsize=(8,6))
plt.plot(x, y, 'o', label='Datos experimentales')
plt.plot(x, y_pred, '-', color='red', label=f'Ajuste lineal: y = {a:.2f} + {b:.2f}x')
plt.xlabel('Carga (kN)')
plt.ylabel('Elongación (mm)')
plt.title('Regresión Lineal: Carga vs Elongación')
plt.legend()
plt.grid(True)
plt.savefig('regresion_carga_elongacion.png', dpi=300)
plt.show()

"""EJERCICIO #2
# Datos del ejercicio
x = np.array([0, 2, 4, 6, 8])         # Posición (cm)
y = np.array([100, 92, 85, 78, 71])   # Temperatura (°C)

# Cálculo de los coeficientes de regresión lineal
n = len(x)
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_xy = np.sum(x * y)
sum_x2 = np.sum(x**2)

b = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
a = (sum_y - b * sum_x) / n

print(f"Coeficientes de la regresión:")
print(f"a (intercepto) = {a:.4f}")
print(f"b (pendiente) = {b:.4f}")

# Predicción usando el modelo
y_pred = a + b * x

# Estimación para x = 5 cm
x_est = 5
y_est = a + b * x_est
print(f"\nTemperatura estimada en x = {x_est} cm: {y_est:.2f} °C")

# Gráfica
plt.figure(figsize=(8,6))
plt.plot(x, y, 'o', label='Datos experimentales')
plt.plot(x, y_pred, '-', color='red', label=f'Ajuste lineal: y = {a:.2f} + {b:.2f}x')
plt.axvline(x_est, linestyle='--', color='gray', label=f'Estimación a x = {x_est} cm')
plt.axhline(y_est, linestyle='--', color='gray')
plt.scatter(x_est, y_est, color='green', zorder=5)
plt.xlabel('Posición (cm)')
plt.ylabel('Temperatura (°C)')
plt.title('Regresión Lineal: Posición vs Temperatura')
plt.legend()
plt.grid(True)
plt.savefig('regresion_temperatura.png', dpi=300)
plt.show()

"""

"""EJERCICIO #3
import numpy as np
import matplotlib.pyplot as plt

# Datos de presión (kPa) y caudal (L/min)
x = np.array([50, 70, 90, 110, 130])
y = np.array([15, 21, 27, 33, 39])

# Cálculo de coeficientes
n = len(x)
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_xy = np.sum(x * y)
sum_x2 = np.sum(x**2)

# Fórmulas de regresión lineal
b = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
a = (sum_y - b * sum_x) / n

print(f"Coeficientes de la regresión:")
print(f"a (intercepto) = {a:.4f}")
print(f"b (pendiente) = {b:.4f}")

# Predicción para x = 100 kPa
x_pred = 100
y_pred = a + b * x_pred
print(f"\nPredicción del caudal para 100 kPa: {y_pred:.2f} L/min")

# Generar valores para la recta
y_fit = a + b * x

# Gráfica
plt.figure(figsize=(8,6))
plt.plot(x, y, 'o', label='Datos experimentales')
plt.plot(x, y_fit, '-', label=f'Ajuste lineal: y = {a:.2f} + {b:.2f}x', color='red')
plt.axvline(x=100, color='gray', linestyle='--', label='Presión = 100 kPa')
plt.axhline(y=y_pred, color='gray', linestyle='--', label=f'Caudal ≈ {y_pred:.2f} L/min')
plt.xlabel('Presión (kPa)')
plt.ylabel('Caudal (L/min)')
plt.title('Regresión Lineal: Caudal vs Presión')
plt.legend()
plt.grid(True)
plt.savefig('caudal_vs_presion.png', dpi=300)
plt.show()

"""