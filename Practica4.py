import numpy as np
matriz_aleatoria=np.random.rand(5,5)
print(matriz_aleatoria)
#Imprimir las posiciones (Fila y columna) de los elementos de la matriz que son mayores que 0.5
print("Los elementos mayores a 0.5 son: \n")
for i in range(0, len(matriz_aleatoria)): 
    temp = len(matriz_aleatoria[i])
    for j in range(0,temp): 
        if matriz_aleatoria[i][j] > 0.5:
            print(f"Elemento en Fila {i}, Columna {j} \n")
