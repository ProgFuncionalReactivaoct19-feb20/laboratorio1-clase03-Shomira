'''Problema 4:

Dado el siguiente listado:

notas = [(5, 5, 10, "Regular"), (10, 2, 4, "Bueno"), (10, 1, 9, "Muy Bueno"), (7, 2, 3, "Sobresaliente")]

Filtrar aquellos que tiene la calificación cualitativa "Regular o Bueno"


'''

#Notas en estado numerico y cualitativo
notas = [(5, 5, 10, "Regular"), (10, 2, 4, "Bueno"), (10, 1, 9, "Muy Bueno"), (7, 2, 3, "Sobresaliente")]
#Funcion lambda y filter que filtra el emncuentro de notas cua;itativas

miFuncion = filter( lambda x: x[3] == "Regular" or x[3]== "Bueno" , notas)
#iMPRESION DE RESULTADOS

print(list(miFuncion))