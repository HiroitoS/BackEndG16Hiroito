# #puedo agrupar varios valores en una variable

# #Listas
# #Que se pueda modificar, es ordenada (maneja indices)

# alumnos = ['Victor', 'Hiroito', 'Marco', 'Angel', 'Bryan', 'Samael', 'Claudia']
# #Las listas empiezan con la posicion 0

# print(alumnos[0])
# print(alumnos[4])

# #Para saber el contenido(longitud) de datos
# #cuenta y no utiliza las posiciones
# print(len(alumnos))

# #si queremos recorrer la lista de derecha a izquierda

# print(len(alumnos[-1]))

# print(alumnos[len(alumnos)-1])


# alumnos.append('Franklin')

# print(alumnos)

# #remover un elementos de la lista

# alumno_eliminado = alumno.pop(3)
# print(alumnos)
# print(alumno_eliminado)
# #del > podemos eliminar variables, eliminar posicionesde la listay otras cosas
# del alumnos[0]
# print(alumnos)
# #cada vez que se elimina una posicion de la lista, todas las demas posisiones ocupan 
# #ese lugar disponible


# #limpiamos todas la lista vacia
# alumnos.claer()
# print(alumnos)


#ejercicio

ejercicio = [1, 2, 3, [4, 5, 6]]


#como puedo devolver el valor de 3
print(ejercicio[2])
#como puedo devolver el valor de 5
print(ejercicio[3][1])

#tuplas
#No se puede modificar y es ordenada(indices)
#Se usa para guardar valores que jamas van a poder cambiar

meses = ('enero', 'Febrero', 'Marzo', 'Abril')

print (meses[0])


data = ('Juan', 'Roberto', [1, 2, 3, ['Eduardo', 'Frank']])

print(data[2][3][0])

#set (conjuntos)
#Desordenada y modificable

colores = {'Negro', 'Blanco', 'Guinda', 'Violeta'}

print(colores)
colores.add('Azul')
print(colores)
print('verde' in colores)
colores.remove('Blanco')

#Diccionarios
#Ordenados PERO por llaves y modificables

persona = {
    'nombre' : 'Eduardo',
    'Edad' : 31,
    'nacionalidad' : 'PERUANO',
    'apellido' : 'De Rivero'
}

# persona.keys(())#llaves
print(persona.values())#valores
print(persona['Edad'])
#print (persona['edades]) JAVASCRIPT si no existe retorna undefined

persona['nombre'] = 'Juancito'
persona['calzado'] = 'Zapatos'#si la llave no existe, entonces la creara
print(persona)


persona = {
    'nombre':"Roberto",
    'edad': 40,
    'hobbies': ['Nada', 'Pescar', 'Jugar videojuegos'],
    'idiomas': [
        {
            'nombre': 'Ingles',
            'nivel': 'Intermedio'
        },
        {
            'nombre': 'Frances',
            'nivel': 'Basico'
        }
    ],
    'habilidades': {'Puntual', 'Economico', 'Proactivo'},
    'debilidades': ('Mentiroso', 'Resentido', 'Comelon')
}
#edad
print(persona['edad'])
#hobbies
print(persona['hobbies'])
#Ultimo hobbie ingresado
print(persona['hobbies'][-1])

#Mostrar los idiomas solo sus nombres
print(persona['idiomas'][0]['nombre'])
print(persona['idiomas'][1]['nombre'])

#ver si es proactivo
# 5.Ver si es proactivo
print('Proactivo' in persona['habilidades'])

#ver cuantas debilidades tiene
print(len(persona['debilidades']))