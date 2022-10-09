
import numpy as np
import pandas as pd

autos=pd.read_csv('/Users/mariaperez-serrabona/PruebaEvaluacion/gestor/ejercicio4/autos.csv', sep='\s+', names=['MPG', 'Cylinders', 'Displacement', 'Horse power',
           'Weight', 'Acceleration', 'Model Year', 'Origin', 'Car Name'])


#print(autos.info())

#4.3.1 ¿Qué coche pesa más de 5000 kg?

autos_mayores_5000 = autos[autos['Weight'] > 5000]
#print(autos_mayores_5000['Car Name'])

#4.3.2 ¿Cuál es el número de cilindros más frecuente en los coches que son del año 76?
autos_76=autos[autos['Model Year']==76]
#print(autos_76['Cylinders'].mode())

#4.3.3 Compara el consumo medio de los coches fabricados en el año 70 con los del año 79 y calcula la diferencia.

autos_70=autos[autos['Model Year']==70]
autos_79=autos[autos['Model Year']==79]

#print(autos_70['MPG'].mean())
#print(autos_79['MPG'].mean())

diferencia=abs(autos_70['MPG'].mean()-autos_79['MPG'].mean())

#print(diferencia)


#4.3.4 Identifica las variables que contienen valores nulos (missing values) en caso que haya alguno.

#print(autos.columns[autos.isnull().any()])

#4.3.5 Consigue un DataFrame de aquellos registros que tengan algún valor nulo (NaN), filtrando el DataFrame original.

null_columns=autos.columns[autos.isnull().any()]
autos[null_columns].isnull().sum()
autos2 = pd.DataFrame(autos[autos.isnull().any(axis=1)])
#print(autos2)

#4.3.6 Calcula la frecuencia del número de cilindros entre los registros del DataFrame anterior (la tabla con valores perdidos).

#print(autos2['Cylinders'].mode())


#4.3.7 Crea un DataFrame de los modelos con 6 o más cilindros, que pesén más de 4000 kg y consumen menos o igual que 10 galón por milla, filtrando el dataset original.
autos_filtrado=autos[(autos['Cylinders']>=6) & (autos['Weight']>4000) & (autos['MPG']<=10)]
#print(autos_filtrado)


def get_datos43():
    print('El coche que pesa más de 5000 kg es: '+ autos_mayores_5000['Car Name'])
    print('El número de cilindros más frecuente en los coches que son del año 76 es: '+str(autos_76['Cylinders'].mode()))
    print('consumo medio de los coches fabricados en 1970: '+str(autos_70['MPG'].mean()))
    print('consumo medio de los coches fabricados en 1979: '+str(autos_79['MPG'].mean()))
    print('Diferencia entre ellos: '+str(diferencia))
    print('Variables con valores nulos: '+autos.columns[autos.isnull().any()])
    print('DataFrame de aquellos registros que tengan algún valor nulo (NaN):')
    print(autos2)
    print('La frecuencia del número de cilindros entre los registros del DataFrame anterior'+ str(autos2['Cylinders'].mode()))
    print('Conjunto de coches con 6 o más cilindros, que pesén más de 4000 kg y consumen menos o igual que 10 galón por milla:')
    print(autos_filtrado)

