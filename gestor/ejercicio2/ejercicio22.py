#2.2.1 Escribe una función que devuelva el número total de carácteres en un listado de cadenas de texto
# y aplícala sobre el ejemplo:
#Entrada a la función: ["PEP 8", "PEP 248", "PEP 257"]

#La salida esperada: 19


def contador_caracteres(lista_cadena_texto):

    count = 0
    for i in lista_cadena_texto:
        for j in i:
            count = count + 1

    print(count)



def get_information22():
    contador_caracteres(["PEP 8", "PEP 248", "PEP 257"])
