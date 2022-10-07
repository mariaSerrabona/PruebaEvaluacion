#4.3.1 ¿Qué coche pesa más de 5000 kg?
#4.3.2 ¿Cuál es el número de cilindros más frecuente en los coches que son del año 76?
#4.3.3 Compara el consumo medio de los coches fabricados en el año 70 con los del año 79 y calcula la diferencia.
#4.3.4 Identifica las variables que contienen valores nulos (missing values) en caso que haya alguno.
#4.3.5 Consigue un DataFrame de aquellos registros que tengan algún valor nulo (NaN), filtrando el DataFrame original.
#4.3.6 Calcula la frecuencia del número de cilindros entre los registros del DataFrame anterior (la tabla con valores perdidos).
#4.3.7 Crea un DataFrame de los modelos con 6 o más cilindros, que pesén más de 4000 kg y consumen menos o igual que 10 galón por milla, filtrando el dataset original.

import numpy as np
import pandas as pd


autos_prueba=pd.read_csv('/Users/mariaperez-serrabona/PruebaEvaluacion/gestor/ejercicio4/autos_prueba_test.csv', sep=';')
autos_prueba.head()

column_names=['mgp', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', ' car name']


autos_prueba=pd.DataFrame(autos_prueba, columns=column_names)

