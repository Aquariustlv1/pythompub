import hangman
import reversegam
import tictactoeModificado
import PySimpleGUI as sg
import json
import os

#**********************************************
archivo="C:\Users\Edwin\Desktop\facu 2020 h\python\documento.txt"

arc=open(archivo,'a')

def Jugador():
	event, values = sg.Window('Ingrese sus datos',
                  [[sg.T('Nombre del Jugador'), sg.In(key='_nombre_')],
                  [sg.B('OK')]]).read(close=True)
	if(values['_nombre_']==""):
		sg.popup('No ha ingresado un nombre')
	else:	
		jugador = values['_nombre_']
		return jugador

def Juego():

	event, values = sg.Window('Juegos',
                  [[sg.T('Seleccione un juego:\n1.-Ahorcado\n2.-Tateti\n3.-Otello\n4.-Salir',font='Any 15'), sg.In(key='_juego_')],
                  [sg.B('Jugar')]]).read(close=True)
	if(values['_juego_']!='1')and(values['_juego_']!='2')and(values['_juego_']!='3')and(values['_juego_']!='4'):
		sg.popup('No ha ingresado un juego')
	else:	
		juego = values['_juego_']
		return juego
	
def leer():
	with open(documento,'r')as archivo:
		datos=json.load(archivo)
	return datos	

def guardar(datos):
	with open(documento,'w')as archivo:
		json.dump(datos,archivo)
		
def actualizar(nombre,juego):
	nombre=nombre.lower()
	if(os.stat(documento).st_size == 0):
		#Si el archivo esta vacio creo el primer elemento
		dic={'Jugados':[]}
		dat={nombre:dic}
		dat[nombre]['Jugados'].append(juego)
	else:
		#Si el archivo ya contiene datos, lo abro y guardo la estructura en la variable dat
		dat=leer()
		#Si el jugador ya existe en el archivo solo actualizo sus datos
		if(nombre in dat.keys()):
			dat[nombre]['Jugados'].append(juego)
		else:
			#Sino existe, lo agrego a la estructura
			dic={'Jugados':[]}
			dat.setdefault(nombre,dic)
			dat[nombre]['Jugados'].append(juego)	
	guardar(dat)		
	
	
def main(args):
		
	sigo_jugando = True
	while sigo_jugando:
		opcion = Juego()
		while(opcion==None):
			opcion=Juego()
		if(opcion!='4'):		
			nombre=Jugador()
			while(nombre==None):
				nombre=Jugador()	
		if(opcion=='1')or(opcion=='2')or(opcion=='3'):	
			if opcion == '1':
				hangman.main()
				juego='Ahorcado'
			elif opcion == '2':
				tictactoeModificado.main()
				juego='Tateti'
			elif opcion == '4':
				reversegam.main()
				juego='Otello'
			actualizar(nombre,juego)	
		elif opcion == '4':
			sigo_jugando = False
		
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
