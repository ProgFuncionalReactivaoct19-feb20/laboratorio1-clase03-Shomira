''''Problema 3:

Dada la siguiente frase:

"No hay medicina que cure lo que no cura la felicidad"

Encuentre el listado que sigue:

["No", "hay", "que", "lo", "que", "no", "la"]
'''
#Creacion de la funcion 

def es_letras(x):
	#Lista con las palabras 
	lista =["No", "hay", "que", "lo", "que", "no", "la"]
	#Realizacion de iteraciones y devielve un boleano
	if x in lista :
		return True
	else:
		return False
#Frase a analizar 
frase = "No hay medicina que cure lo que no cura la felicidad"
#Split que dividir la frase
resultado = frase.split( )
#Funcion dentro de otra funcion
resultado2 = filter(es_letras, resultado)
#iMPRESION DE RESULTADOS ...lista de palabras encontradas
print(list(resultado2))
