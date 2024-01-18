numero = 10

# try (intentalo)
# y si es que falla entonces capturo el error con una except (exception)
try:
    print(10/0)
# si ingresa a un except ya no ingresa a los demas siempre se recomienda dejar el except 
    #mas generico(exception) al final para evitar ingresos innecesarios
except ZeroDivisionError:
    #si el errore es de tipo de division entre 0 entonces ingresa aca
    print('no se puede dividir entre 0')

except Exception as error:
    #ver que es el causante del error
    print(error.args)
    #ver
    print(type(error))
    print('Operacion incorrecta')

print('otro codigo')


#Lambda Function / Funciones Anonimas
#funcion no recibe ningun parametro y retorna el valor de 1

resultado = lambda valor1, valor2, valor3: valor1 + valor2 + valor3
print(resultado(10,20,30))



# crear una funcion que reciba dos numeros y que devuleva cual es el mayor, si el usuario ingresa in valor que no sea un numero entonces volver a 
#pedirselo que sea un numero

def numeroMayor(numero1, numero2):
    #forma 1
    if numero1 > numero2:
        return numero1
    else:
        return numero2
    
    #forma 2
    return numero1 if numero1 > numero2 else numero2

#



while True:
    try :
        numero1= int(input('Ingresa el primero numero'))
        numero2= int(input('Ingresa el segundo numero'))
        resultado = lambda numero1, numero2: numero1 if numero1 > numero2 else numero2
        print('El numero mayor es {}'.format(resultado(numero1, numero2)))
        break
    except:
        print('Tienes que ingresar solo numeros')