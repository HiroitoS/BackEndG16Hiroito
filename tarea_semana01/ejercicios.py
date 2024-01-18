# Ejercicios 1
print('---------------Ejercicio 1------------------')
# n = int(input('Please, enter a number :'))

# if numero % 2 == 0:
#     if(numero <= 5 and numero >20):
#         print('The number is not weird')
#     else:
#         print('The number is weird')
# else:
#     print('The number is weird')
# if n % 2 == 0:
#         if n <= 5 or n > 20:
#             print('Not Weird')
#         else:
#             print('Weird')
# else:
#     print('Weird')

print('--------------------------------------------')

#ejercicio 2
print('---------------Ejercicio 2------------------')



# i=0
# numero=[]
# n=int(str(input()))
# if n > 0 and n < 10:
#     while i<int(n):   
#         valor=str(input())
#         numero.append(valor)
#         i=i+1
#     for m in numero:
#         try:
#             print(int(n)/int(m))
#         except ZeroDivisionError as e:
#                 print(f"Código de error: {e}")
#         except ValueError as v:
#                 print(f"Código de error: {v}")
# else:
#      print('El numero tiene que ser mayor a 0 o menor a 10')

print('-----------------------------------------')
import numpy as np
def arrays(arr):
    # complete this function
    # use numpy.array
    ar= np.array([], float)
    
    for element in arr:
        ar = np.append(ar,element)
        inv = ar[::-1]
    num = np.array(inv,float)
    return num

a = []
for _ in range(6):
    arr = input().strip().split(' ')
    a.append(arr)
result = arrays(a)
print(result)