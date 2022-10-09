#4.3.2 ¿Cuál es el número de cilindros más frecuente en los coches que son del año 76?
#4.3.3 Compara el consumo medio de los coches fabricados en el año 70 con los del año 79 y calcula la diferencia.
#4.3.4 Identifica las variables que contienen valores nulos (missing values) en caso que haya alguno.
#4.3.5 Consigue un DataFrame de aquellos registros que tengan algún valor nulo (NaN), filtrando el DataFrame original.
#4.3.6 Calcula la frecuencia del número de cilindros entre los registros del DataFrame anterior (la tabla con valores perdidos).
#4.3.7 Crea un DataFrame de los modelos con 6 o más cilindros, que pesén más de 4000 kg y consumen menos o igual que 10 galón por milla, filtrando el dataset original.

import numpy as np
import pandas as pd

autos=pd.read_csv('/Users/mariaperez-serrabona/PruebaEvaluacion/gestor/ejercicio4/autos.csv', sep='\s+', names=['MPG', 'Cylinders', 'Displacement', 'Horse power',
           'Weight', 'Acceleration', 'Model Year', 'Origin', 'Car Name'])


print(autos.info())

#4.3.1 ¿Qué coche pesa más de 5000 kg?

autos_mayores_5000 = autos[autos['Weight'] > 5000]
print(autos_mayores_5000['Car Name'])

#4.3.2 ¿Cuál es el número de cilindros más frecuente en los coches que son del año 76?
autos_76=autos[autos['Model Year']==76]
print(autos_76['Cylinders'].mode())