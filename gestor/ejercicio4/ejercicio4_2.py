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
