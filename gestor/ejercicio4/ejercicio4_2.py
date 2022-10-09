from array import array
from dataclasses import dataclass
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
#4.2.1
def convert_array(array):
    for m in range(len(array)):
        array[m]=int(array[m])

    conversor=lambda x: pd.Series(x)
    return conversor(array)
#4.2.2
def convertir_datos():
    arr=[10, True, 8.00, False, 8, 10]
    data=convert_array(arr)
    return data
data=convertir_datos()
#4.2.3
def obtener_datos_serie():
    #VALORES DE LA SERIE
    #print(data.values)
    #INDICES

    #TIPO DE DATOS
    #print(data.dtypes)
    #NUMERO DE BITS EN MEMORIA
    #print(data.values.itemsize)
    return data.values, data.dtypes,data.values.itemsize
#4.2.4 GRAFICO
print(obtener_datos_serie())
#4.2.5
def get_estadisticas():
    return data.describe()
#4.2.6
def sacar_frecuencia_y_val_unicos():
    dic={}
    for i in data:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    #4.2.7
    lista=[]
    for i in dic:
        if dic[i]==1:
            lista.append(i)
    return dic, lista

#4.2.8
def reordenar_reset():
    #print(data.sort_values(ascending=False).reset_index(drop=True))
    return data.sort_values(ascending=False).reset_index(drop=True)
#4.2.9
def get_df():
    dataej_42 = pd.DataFrame(data)
    dataej_42.columns=['Ej_42']
    #print(dataej_42)
    return dataej_42
