alumnos = ['Angel', 'Bryan', 'Carlos', 'Hiroito', 'Clauida', 'Samael', 'Marco']

for alumno in alumnos:
    print(alumno)

#for se puede utilizar con string(textos)
#forma 1
frase = 'No hay mas que por bien no venga'
for letra in frase:
#     if letra == ' ':
#         pass
#     else:
#         print(letra)
#forma 2 
#     if letra !=' ':
#         print(letra)
# # forma 3
#     #continue> termina el ciclo actual(la iteracion en camion) y no permite hacer nada 
#     #mas luego del continue
#     continue
    # if letra ==' ':
    #     continue
    # print(letra)
#forma 4
#para definir una variable y esta no queremos colocarle un valor inciial podemos usar la palabra None
# Si ni queremos realizar nada en un operador ternario podemos colocarlo ahi
    None if letra== ' ' else print(letra)
print('------------')

# range > si quiero realizar un for manual sin iso de listas, tuplas , set o textos
# range limite > el for se ejecutara hasta el valor sea menor que el tope(limite)
for numero in range(4):
    print(numero)

print('------------')
#range (inicio,limite)
for numero in range(1,4):
    print(numero)

print('------------')

#range (inicio, limite, ingrementa/decrementa)
for numero in range(1,10,2):
    print(numero)
print('------------')
texto = 'Hola me llamo eduardo'
vocales = ['a', 'e', 'i', 'o', 'u']
a=0
for letra in texto:
    if letra in vocales:
        a = a + 1
print('Hay', a ,'vocales')
# donde tengamos {} ahi colocaremos una variable que puede ser de todo tipo
print ('Hay {} vocales'.format(a))
# al colocar la f antes de las comillas estaremos indicando que lo que vaya dentro de las 
#variables 
print(f'Hay {a} vocales')

# %s que convirte el calos que le vamos a pasar
print('Hay %s vocales' % a)
# print('j' in vocales)
# print('e'in vocales)
# iterar la variable texto y ver cuantas vocales hay
#respuesta : hay 9 vocales



# % (modulo)
print(99/5) # cociente 
print(99%5) # residuo entero
print(99//5) # cociente entero sin uso de decimales

print('---------------------')
n=range(1,56)
#quiero saber cuantos numero pares tengo
p=0
for numero in n:
    if numero % 2 == 0:
        p = p + 1
        print(numero)
print('Hay ', p , ' numeros pares')


