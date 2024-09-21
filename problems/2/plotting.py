import time
import matplotlib.pyplot as plt
from solve import solve_base_dynamic, solve_with_shortcuts
from test import generate_case
import random
import math

# Lista de diferentes valores para n
valores_n = list(range(1,20))  # Cambia el rango según sea necesario

# Listas para almacenar los tiempos de ejecución
tiempos_funcion_1 = []
tiempos_funcion_2 = []

# Medir el tiempo de ejecución para cada función
for n in valores_n:
    A,B,p,k=generate_case()
    k=10
    p=n
    # Medir tiempo para funcion_1
    inicio = time.time()
    a=solve_base_dynamic(A,B,p,k)
    fin = time.time()
    tiempos_funcion_1.append(fin - inicio)

    # Medir tiempo para funcion_2
    inicio = time.time()
    b=solve_with_shortcuts(A,B,p,k)
    fin = time.time()
    tiempos_funcion_2.append(fin - inicio)

    if a!=b:
        print("Resultados desiguales para test:")
        print(A,B,p,k)
        exit()

# Graficar los resultados
plt.figure(figsize=(10, 6))
plt.plot(valores_n, tiempos_funcion_1, label='Función 1', marker='o')
plt.plot(valores_n, tiempos_funcion_2, label='Función 2', marker='x')
plt.title('Comparación para n=100 y k=10')
plt.xlabel('Valor de p')
plt.ylabel('Tiempo (segundos)')
plt.legend()
plt.grid(True)
plt.show()
