import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/user/Documents/USA/S6/Toma de decisiones/BD_Bancos2.csv",sep=";",encoding='unicode_escape')  #df = data frames

'''
print(df.head()) #imprime los 5 primeros datos
print(df.index) #imprime la cantidad de filas
print(df.columns) #imprime una lista (objeto de dataframes) con los encabezados
'''

#nombre_entidad = df['NOMBREENTIDAD'].value_counts() #cuáles son las categorías que hay en esa columna y cuántas filas tienen ese valor, para datos cualitativos
#print(nombre_entidad)

'''
1. Borrar datos nulos
2. Datos atípicos o sin sentido
'''
print(df.columns)

#df['CODIGOENTIDAD'].value_counts().plot.bar()
#df['TOTAL_TARJETAS'].plot.hist()
#plt.show()

#nombre_entidad = df['NOMBREENTIDAD'].value_counts()
#tipo_entidad = df['TIPOENTIDAD'].value_counts()
#nombre_uca = df['NOMBRE_UCA'].value_counts()
#print(nombre_entidad)
#print(tipo_entidad)
#print(nombre_uca)
#df['NOMBREENTIDAD'].value_counts().plot.bar()
#plt.show()

df['PERSONA_NATURAL'].plot.hist()
plt.show()


df['PERSONA_JURIDICA'].plot.hist()
plt.show()

df['TOTAL_TARJETAS'].plot.hist()
plt.show()