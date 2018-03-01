#coding: utf-8
num = int(input("Cuantas palabras quieres introducir: "))
while num<0:
	num = int(input("Tiene que ser mayor que 0. Pruebe again: "))
diccionario = {} 
dicing = []
dicesp = []
for i in range(num):
	key = raw_input("Introduce palabra: ")
	valuees = raw_input("Introduce definicion para español: ")
	dices += [valuees]
	valuein = raw_input("Introduce definicion para inglés: ")
	
