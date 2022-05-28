#!/usr/bin/env python
# coding: utf-8

# # Introduccion a NumPy - Ejercicios
# Empezamos a trabajar como data Analyst en una empresa de la ciudad, y el gerente requiere de nuestra ayuda...

# #### 1. Comienza importando NumPy como `np`

# In[ ]:
import numpy as np




# La empresa recaba datos de usuarios de internet: 
# - 'duracion,paginas,acciones,valor,clase'. 
# 
# Por ejemplo, un usuario navega: |duracion|paginas|acciones|valor|clase|, o sea:
# 
# |2.34 minutos/segundos de navegación |8 páginas|4 acciones|1 valor|5 (clasificación de usuario)|
#     
# #### 2.Crea un array de NumPy que represente los datos anteriores. Cada elemento debe ser un numero (por ejemplo `2.34` para "2.34 minutos/segundos"). Guarda este array como `un_usuario`

# In[ ]:
datos_usuario = [2.34,8,4,1,5]
un_usuario = np.array(datos_usuario)



# El asistente ha compilado los datos de un día en un archivo `csv` llamado `usuarios.csv`. Este archivo fue suministrado.
# 
# #### 3. Carga este archivo en una variable llamada `usuarios`

# In[ ]:
import pandas as pd
usuarios = np.genfromtxt ('usuarios.csv', delimiter=",")

# #### 4. Emite 'usuarios'

# In[ ]:
print(usuarios)



# Cada fila representa un usuario diferente. Cada columna representa una característica diferente.
# 
# La tercera columna representa el numero de 'acciones' que realiza cada usuario. 
# 
# #### 5. Selecciona todos los elementos de la tercera columna y guárdalos en una variable llamada 'acciones'

# In[ ]:

acciones = usuarios[:,2:3]
print(acciones)




# #### 6. Cuáles usuarios realizaron 4 acciones? Usa una sentencia lógica para obtener 'True' o 'False' para cada valor de acciones

# In[ ]:

print(acciones==4)



# El gerente necesita los datos de la tercera fila...
# 
# #### 7. Crea una variable para los datos de la tercera fila y emite los datos

# In[ ]:

datos_tercer_fila = usuarios[4:5,:]
print(datos_tercer_fila)



# #### 8. Los datos del quinto usuario se guardaron mal, en realidad es el doble en todo. Guarda la operación en nueva variable en  'doble_usuario5'

# In[ ]:

datos_tercer_fila_x2 = datos_tercer_fila*2
print(datos_tercer_fila_x2)



# #### 9. El gerente necesita saber de cuántos usuarios se obtuvo información:

# In[ ]:

total_usuarios = len(usuarios[:,0:1])
print(total_usuarios)



# #### 10. Cómo quedó muy contento con nuestro trabajo necesita saber:
# 
# 1. El máximo de tiempo que estuvo un usuario navegando.
# 2. El mínimo de tiempo que estuvo un usuario navegando.
# 3. La media de tiempo de navegación y de páginas navegadas.
# 4. El total de tiempo de navegación y de páginas navegadas.
# 5. La mediana de acciones registradas.
# 6. Calcula la moda de las acciones (puedes necesitar: from scipy import stats)

# In[ ]:

# 1. El máximo de tiempo que estuvo un usuario navegando.
max_t_navega = (usuarios[:,0:1]).max()
print(max_t_navega)
# 2. El mínimo de tiempo que estuvo un usuario navegando.
min_t_navega = (usuarios[:,0:1]).min()
print(min_t_navega)
# 3. La media de tiempo de navegación y de páginas navegadas.
#de las 2 formas da:
media_t_navega = (usuarios[:,0:1]).mean()
print(media_t_navega)
media_t_navega = np.mean(usuarios[:,0:1])
print(media_t_navega)
media_paginas = (usuarios[:,1:2]).mean()
print(media_paginas)
# 4. El total de tiempo de navegación y de páginas navegadas.
#de las 2 formas da:
total_t_navega = (usuarios[:,0:1]).sum()
print(total_t_navega)
total_t_navega = np.sum(usuarios[:,0:1])
print(total_t_navega)
total_paginas = (usuarios[:,1:2]).sum()
print(total_paginas)
# 5. La mediana de acciones registradas.
mediana_acciones = np.median(usuarios[:,2:3])
print(mediana_acciones)
# 6. Calcula la moda de las acciones (puedes necesitar: from scipy import stats
from scipy import stats
moda_acciones = stats.mode(usuarios[:,2:3])
print(moda_acciones)
