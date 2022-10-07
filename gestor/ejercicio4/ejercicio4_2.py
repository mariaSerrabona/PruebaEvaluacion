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
arr=[10, True, 8.00, False, 8, 10]
data=convert_array(arr)
#4.2.3
#VALORES DE LA SERIE
print(data.values)
#INDICES

#TIPO DE DATOS
print(data.dtypes)
#NUMERO DE BITS EN MEMORIA
print(data.values.itemsize)

#4.2.4

#4.2.5
print(data.describe())
#4.2.6
dic={}
for i in data:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
print(dic)
#4.2.7
for i in dic:
    if dic[i]==1:
        print (i)
print()
#4.2.8

print(data.sort_values(ascending=False).reset_index(drop=True))
#4.2.9
dataej_42 = pd.DataFrame(data)
dataej_42.columns=['Ej_42']
print(dataej_42)
