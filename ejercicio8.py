
numeros_primos=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
#me complique buscando una fucion predefinida que me devolviera si era o no primo :( jajaja , 
#igual no se si este bien del todo o si habia que implementar el algoritmo de si es primo o no , lo que hice fue asignar a un arreglo
#los numeros primos entre el 1 y el 100 para no complicarme la vida jaja :D
palabra=input('ingrese una string   ')
pal=palabra
palabra=palabra.lower()
letras_procesadas=[]
letras_primas=[]
for n in range(len(palabra)):
	if palabra[n] not in letras_procesadas:
		letras_procesadas.append(palabra[n])
print('\n')
print('\n')
print(pal)
for n in letras_procesadas:
	if palabra.count(n)== 1:
		print('La letra '+ n + ' aparece: ' + str(palabra.count(n))+' vez')
	else:
		print('La letra '+ n + ' aparece: ' + str(palabra.count(n))+' veces')
		#si es distinto a 1 me fijo si esta dentro de la lista numeros_primos para agregarlo a la lista letras_primas
		if palabra.count(n) in numeros_primos:
			letras_primas.append(n)
if letras_primas:
	if len(letras_primas) == 1:
		parte1="Por lo tanto la letra  ' "+letras_primas[0]
		parte2=" ' es la letra que aparece un número primo de veces."
		print(parte1 + parte2)
	elif len(letras_primas) == 2:
		parte1="Por lo tanto las letras '"+letras_primas[0]+"' e '"+letras_primas[1]
		parte2="' son letras que aparecen un número primo de veces."
		print(parte1 + parte2)
	else:
		parte1="Por lo tanto las letras ' "
		parte2=" ' son letras que aparecen un número primo de veces."
		for n in letras_primas:
			parte1=parte1 + n +','
		parte1=parte1 + '|'
		parte1 = parte1.replace(",|","")
		print(parte1 + parte2)
else:
	print('no hay letras que aparezcan un numero primo de veces')



#indagando en internet encontre un algoritmo que creo que es el indicado ,tendria que modificar mi codigo
#en pseudocodigo una condicion seria si el numero de veces que aparece el caracter es menor a 1 entonces  no es primo
#o si el numero de veces que aparece el caracter es es  igual 2  estonces seria primo
#y sino haria un for  con un  rango desde 2 a la cantidad de ocurrencias del caracter el cual tendria que ser mayor a 2 obio evaluando con el operador resto %
# si el resto entre la cantidad de veces que aparece el caracter y un valor dentro del rango me da 0  entonces no es primo sino si lo es 
