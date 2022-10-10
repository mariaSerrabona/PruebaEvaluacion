#3.1.1 Crea un array de tamaño (6x6) con elementos aleatorios entre 0 y 10 inclusive.
import numpy as np

array_multidimen_aleatorio=np.random.randint(1, 10, size=(6, 6))


#3.1.2 Calcula el total de bytes que ocupa la matriz.
array_bytes=array_multidimen_aleatorio.nbytes

#3.1.3 Calcula la media y la desviación estándar de los valores presentes en la matriz.

#media
media=np.mean(array_multidimen_aleatorio)

#desviación estándar

desv_estandar=np.std(array_multidimen_aleatorio)


#3.1.4 Crea un nuevo array del mismo tamaño que contenga elementos aleatorios con una distribución normal con la misma media y la misma desviación estándar que el array original.

array_multidimen_aleatorio_normal=np.random.normal(media, desv_estandar, size=(6, 6))


#3.1.5 Crea un nuevo vector, convirtiendo todos los valores del array creado en el paso anterior en números enteros.

array_multidimen_aleatorio_int = array_multidimen_aleatorio_normal.astype(int)

array_multidimen_aleatorio_int=array_multidimen_aleatorio_int.flatten()



def get_information_31():
    print('Un array de tamaño (6x6) con elementos aleatorios entre 0 y 10 inclusive:')
    print(array_multidimen_aleatorio)

    print('el total de bytes que ocupa la matriz:')
    print(array_bytes)

    print('media y la desviación estándar de los valores presentes en la matriz:')
    print(media)
    print(desv_estandar)

    print('nuevo array del mismo tamaño que contenga elementos aleatorios con una distribución normal con la misma media y la misma desviación estándar que el array original.')
    print(array_multidimen_aleatorio_normal)

    print('nuevo vector, convirtiendo todos los valores del array creado en el paso anterior en números enteros.')
    print(array_multidimen_aleatorio_int)
