from tkinter.tix import COLUMN
import pandas as pd
d = {'Nombre':pd.Series(['Tomy','Juan','Ricky','Vilma','Silvio','Sara','José']),
'Edad':pd.Series([25,26,25,23,30,29,23]),
'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}
df = pd.DataFrame(d)
print ("Nuestro objeto es:")
print(df)
print ("El número total de elementos en nuestro objeto es:")
print(df.size)


d = {'Nombre':pd.Series(['Tomy','Juan','Ricky','Vilma','Silvio','Sara','José']),
'Edad':pd.Series([25,26,25,23,30,29,23]),
'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}
df = pd.DataFrame(d)
#df = df.style.hide_index()
df = df.set_index('Nombre')
print ("Nuestro objeto es:")
print(df)
print ("El número total de elementos en nuestro objeto es:")
print(df.size)


