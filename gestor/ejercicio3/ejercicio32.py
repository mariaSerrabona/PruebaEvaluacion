# 3.2.1 Crea un array de tamaño (3x4) de todos los números enteros entre 0 y 100 que sean múltiplos de 9.
import numpy as np
import random

lista = []
for i in range(0,100):
    if i % 9 == 0:
        lista.append(i)
n=4
sep=[lista[i:i + n] for i in range(0, len(lista), n)]
array = np.array(sep)
print(array)

# 3.2.2 Filtra todos los valores del vector creado en el paso anterior de la siguiente manera:
# Si son valores positivos y múltiplos de 5 se conservan sin cambios

# En el caso contratio se sustituyen con el valor -1

for i in array:
    if i > 0 and i % 5 == 0:
        print(i)
    else:
        i = (-1)*i
        print(i)


def get_information_32():
    print('Un array de tamaño (3x4) de todos los números enteros entre 0 y 100 que sean múltiplos de 9:')
    print(array)

    print('Si son valores positivos y múltiplos de 5 se conservan sin cambios:')
    print(i)

    print('En el caso contratio se sustituyen con el valor -1:')
    print(-i)


