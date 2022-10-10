
def seleccion(lista):
    longitud = (len(lista)-1)
    lista2 = []
    for i in range (longitud, 0, -2):
        lista2.append(lista[i])
    if len(lista)%2 != 0:
        lista2.append(lista[0])
    return print(lista2)

def cambio_pos (lista):
    elemento_1 = lista[0]
    elemento_final = lista[len(lista)-1]
    lista[0] = elemento_final
    lista[len(lista)-1] = elemento_1

    return print(lista)

def eliminar (lista):
    cambio_pos(lista)

    del lista[len(lista)-1]
    return print(lista)

def repetidos (lista):
    duplicados = [x for i, x in enumerate(lista) if i != lista.index(x)]
    return (duplicados)

def get_information11():
    print('Vamos a ultilizar la siguiente lista: [True, 9, 9.99, hola ,8,9,0,8,5]')
    #Ejercicio 1.1.2
    seleccion([True, 9, 9.99, 'hola',8,9,0,8,5])

    #Ejercicio 1.1.3
    print(cambio_pos([True, 9, 9.99, 'hola']))

    #Ejercicio 1.1.4
    eliminar([True, 9, 9.99, 'hola'])

    #Ejercico 1.1.5
    repetidos([1,2,2,3,4,5,5])



