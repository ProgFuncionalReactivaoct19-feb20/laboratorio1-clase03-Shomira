'''Problema 2:

Dada la siguiente lista:

notas = [(5, 5, 10), (10, 2, 4), (10, 1, 9), (10, 2, 3)]

En contrar una lista como sigue:

[20, 16, 20, 15]

'''
#Datos 
notas = [(5, 5, 10), (10, 2, 4), (10, 1, 9), (10, 2, 3)]
#posiciones datos para sumar
num1 = lambda x :x [0]
num2 = lambda x :x [1]
num3 = lambda x :x [2]

#Funcion que suma los dtaos en ciertas psoiciones

funcion = lambda x: (num1(x) +num2(x)) +( num3(x))

#Impresion de Lista 
print(list(map(funcion, notas)))
