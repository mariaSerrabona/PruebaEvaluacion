#2.1.1 Recorre el listado del ejemplo y realiza las siguientes operaciones: [18, 50, 210, 80, 145, 333, 70, 30]
# Imprimr el número en caso de que sea múltiplo de 10 y menor que 200

# Parar el programa si llega a un número mayor que 300

class ejercicio21:

    def listado(lista):
        for numero in lista:
            while numero < 300:
                if numero % 10 == 0 & numero < 200:
                    print(numero)


#listado([18, 50, 210, 80, 145, 333, 70, 30])




