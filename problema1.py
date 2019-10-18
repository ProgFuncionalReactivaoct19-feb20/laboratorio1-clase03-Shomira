#Problema 1:

''''Dado el siguiente conjunto de promedios de estudiantes; determinar los estudiantes que pasan de ciclo. 
Todos los estudiantes que pasan de ciclo son aquellos que tienen un promedio de 16.5 o mayor.

promedios.txt'''
#[10,20,18,19,20,17,18,16,16,11,12,13]


#Importacion del archivo
from datos import*

archivo= open ( "datos\promedios.txt", "r")
promedios = filter(lambda x: x >= 16.5, archivos

print(list(promedios))


