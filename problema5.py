'''Problema 5:


Dadas las siguientes edad:

[10, 12, 13, 14, 16, 18, 20, 30, 31, 32, 33, 40, 50]

Se ha generado una lista denomindad black_edades, formada así:

[10, 14, 30, 32, 40, 16]

Generar el listado de edades que no estén dentro de las black_edades.
'''

#Lista General
edad = [10, 12, 13, 14, 16, 18, 20, 30, 31, 32, 33, 40, 50]
#Lista black

lista_black = [10, 14, 30, 32, 40, 16]

#Funcion anonima que filtra los de la lista black excluyendoloss
funAnonima = filter (lambda x: x != lista_black[x], edad )

print(list(funAnonima))


