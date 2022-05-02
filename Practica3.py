#Generar una matriz de 7 por 9. Las primeras 3 columnas de la matriz tienen que tener el valor 0. La cuarta columna 
#debe tener el valor 0.5, excepto por el último valor de esa columna, que tiene que ser 0.7. Las otras tres columnas 
#deben tener el valor 1. Luego imprimir la matriz. Imprimir también el promedio de la última fila.

import numpy as np
a = np.zeros((7, 9))
print(a)
a[:6,3:4] = a[:6,3:4]+0.5
print(a)
a[6:,3:4] = a[6:,3:4]+0.7
print(a)
a[:,4:] = a[:,4:]+1
print(a)
print(np.mean(a[6:,:])) 
