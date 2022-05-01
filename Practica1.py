import numpy as np
lista_de_listas=[ [-44,12], [12.0,51], [1300, -5.0]]
a = np.array(lista_de_listas)
print("Matriz original")
print(a)
# Restarle 5 a la fila 2 de la matriz
a[2] = a[2]-5 
print(a)
# Multiplicar por 2 toda la matriz
a = a*2
print(a)
# Dividir por -5 las dos primeras filas de la matriz
a[:2] = a[:2]/(-5)
print(a)
#Imprimir la última fila de la matriz
ultima_fila= a[2]
print(ultima_fila)
