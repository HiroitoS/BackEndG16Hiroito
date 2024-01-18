
edad = 16
nacionalidad = 'venezolano'
# if > si
if edad > 18 and nacionalidad == 'peruano':
    print('Puedes votar')
#else sino
    
else:
    print('Llamare a tus padres')


if edad > 18 or nacionalidad == 'peruano':
    print('Puedes votar')
#else sino
    
else:
    print('Llamare a tus padres')




if edad > 18:
    print('Puedes votar')
#elif sino si
elif edad > 15:
    print('Ya te falta poco para votar')
else:
    print('Que haces aqui?')


# Segun el sexo y la estatura hacer lo siguiente
# si es Masculino
    # si mide mas de 1.50 entonces indicar que no hay prendas
    # si mide entre 1.30 y 1.49 indicar que si hay ropa
    # si mide menos de 1.30 indicar que no hay prendas
# si es Femenino
    # si mide mas de 1.40 indicar que no hay prendas
    # si mide entre 1.10 y 1.49 indicar que si hay
    # si mide menos de 1.10 indicar que no hay
sexo = 'Femenino'
estatura = 1.20

if sexo == 'Masculino':
    if estatura > 1.30 and estatura< 1.49:
        print('si hay ropa para hombres')
    else:
        print('no hay ropa para hombres')
else:
    if sexo == 'Femenino':
        if estatura >= 1.10 and estatura<= 1.49:
            print('si hay ropa para mujeres')
        else:
            print('no hay ropa para mujeres')
 

 #operador TERNARIO
#es una condicion para ejecutarse en una sola linea y en base a la condicacion
#retornara un valor u otro
            
# Siel usuario es pareuano pagara 5 soles si es extranjero pagara 8 soles
nacionalidad = 'Ecuatoriano'    
if nacionalidad == 'Peruano':
    print('Pague 5 soles')
else:
    print('pague 8 soles')


# valor si es verdadero      if condicional (es)          else resultado si es false
resultado = 'pague 5 soles' if nacionalidad == 'Peruano' else 'pague 8soles'
print(resultado)