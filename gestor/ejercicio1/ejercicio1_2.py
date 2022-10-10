dic_ejemplo = {'Alumnos': ["Carlos", "Ana", "Daniela", "Martín"],

'Curso': "Big Data",

'Edad': ('22', '21', '20', '22'),

'Presencial': True

}
#1.2.1
def edad_alumno(alumno):
    print (dic_ejemplo['Edad'][dic_ejemplo['Alumnos'].index(alumno)])
    return dic_ejemplo['Edad'][dic_ejemplo['Alumnos'].index(alumno)]
#1.2.2
def Se_Encuentra(clave):
    devolver=True
    if clave not in dic_ejemplo:
        devolver=False
    print (devolver)
    return devolver

#1.2.3
def valor_asociado_y_longitud(clave):
    print (type(dic_ejemplo[clave]), len(dic_ejemplo[clave]))
    return type(dic_ejemplo[clave]), len(dic_ejemplo[clave])

#1.2.4
def tamaño_set_Edades():
    sett=set(dic_ejemplo['Edad'])
    print (len(sett))
    return len(sett)
