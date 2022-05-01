import numpy as np
#Calcular la suma de los elementos de a (ejercicio anterior) utilizando dos fors anidados
lista_de_listas=[ [-44,12], [12.0,51], [1300, -5.0]]
a = np.array(lista_de_listas)
suma = 0
for i in a[:]: 
    for n in a[i,]: 
        print(n, end=' ')
    print('\n')
print(suma)
# Calcular la suma de los elementos de a utilizando np.sum
np.sum(a)
# Calcular el promedio de los elementos de las primeras dos filas de a utilizando dos fors anidados
promedio=0
promedio = np.sum(a[:2])/ a[:2].size
print(promedio)
# Calcular el promedio de los elementos de las primeras dos filas de utilizando slices (notación (:)) y np.mean
#IMPLEMENTAR
