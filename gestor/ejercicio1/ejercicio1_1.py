class Lista:
    def __init__(self):
        self.lista = []

    def __str__(self) :
        return "Lista: {}".format( self.lista )

def seleccion(lista):
    longitud = (len(lista)-1)
    for i in range (longitud, 0, -2):
        lista2 = lista[i])
    return lista2

def cambio_pos (lista):
    elemento_1 = lista[0]
    elemento_final = lista[len(lista)-1]
    lista[0] = elemento_final
    lista[len(lista)-1] = elemento_1

    return lista

def eliminar (lista):
    nueva_lista = cambio_pos(lista)

    del nueva_lista[len(nueva_lista)-1]
    return nueva_lista

def repetidos (lista):
    duplicados = [x for i, x in enumerate(lista) if i != lista.index(x)]
    return duplicados



def main():
    lista = [True, 9, 9.99, 'hola']
    print (seleccion(lista))
    print(cambio_pos(lista))
    print(eliminar(lista))


    lista_2 = [1,2,2,3,4,5,5]
    print(repetidos(lista_2))



if __name__ == '__main__':
    main()

