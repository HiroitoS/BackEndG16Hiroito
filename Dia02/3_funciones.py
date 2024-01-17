# def > definition
# toda funcionnpuede recibir parametros
# toda funcion puede devolver un resultado

def saludar():
    print('Hola buenas noches!')

# Si la funcion no esta definida no esta siendo implementada(llamada) el
#codigo dentro  de la funcion nunca se ejecutara

saludar()

def sumar(numero1 , numero2):
    resultado = numero1 + numero2
    print('La suma es ', resultado)

sumar(10, 20)

def multiplicar(numero1 , numero2):
    resultado = numero1 * numero2
    return resultado

resultado_multiplicacion = multiplicar(50, 20)
print(resultado_multiplicacion)

# si queremos colocar un parametro por defecto entonces los parametros por defecto SIEMPRE
#van al final
def saludarCordialmente(nombre, cargo='Siñorsh'):
    return 'Buenas noches {} {}'.format(cargo, nombre)

print(saludarCordialmente('Juancito'))
print(saludarCordialmente('Sofia', 'Damicela'))

print(saludarCordialmente(cargo='Gerente', nombre='Raul'))

# el * al momento de definir una funcion indicaremos que esta peude recibir n valores
# ards> significa arguments
def sumarNumeros(*args):
    #devolver la sumatoria de todos los valores que recibe args
    
    resultado = 0
    for num in args:
        
        resultado = resultado + num
    
    return resultado

resultado = sumarNumeros(10,20,30,40,50,60,70,80,90,110)
print(resultado)


#sirve para recibir un numero ilimitado de parametros
# kwargs >keyboard arguments
def capturarPersona(**kwargs):
    return kwargs



resultado = capturarPersona(nombre='Hiroito', apellido = 'Sanchez', 
                correo='hitoito.sanchez@gmail.com',estatura = 1.70)

print(resultado)

data= {'nombre': 'Hiroito', 'apellido': 'Sanchez', 
       'correo': 'hitoito.sanchez@gmail.com', 
       'estatura': 1.7} 
# en el metodo .get solo sirve para devolver informacion mas no para asignar nuevos valores
print(data.get('apellido'))
data['edad'] = 30
# no se puede usar el metodo .get para cuestiones de asignacion
print('hola')