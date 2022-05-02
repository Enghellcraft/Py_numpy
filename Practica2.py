import numpy as np
#Calcular la suma de los elementos de a (ejercicio anterior) utilizando dos fors anidados
lista_de_listas=[ [-44,12], [12.0,51], [1300, -5.0]]
a = np.array(lista_de_listas)
suma = 0
for i in range(0, len(a)): 
    temp = len(a[i])
    for j in range(0,temp): 
        suma = suma + a[i][j]
print(suma)
# Calcular la suma de los elementos de a utilizando np.sum
np.sum(a)
print(suma)
# Calcular el promedio de los elementos de las primeras dos filas de a utilizando dos fors anidados
promedio=0
cont = 0
suma = 0
for i in range(0, len(a[:2,:])): 
    temp = len(a[i])
    for j in range(0,temp): 
        suma = suma + a[i][j]
        cont = cont + 1
promedio = suma / cont
print(promedio)
# Calcular el promedio de los elementos de las primeras dos filas de utilizando slices (notación (:)) y np.mean
promedio = np.mean(a[:2,:])
print(promedio)
