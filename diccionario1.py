#coding: utf-8
num = int(input("Cuantas palabras quieres introducir: "))
while num<0:
	num = int(input("Tiene que ser mayor que 0. Pruebe again: "))
diccionario = {}
for i in range(num):
	key = raw_input("Introduce palabra: ")
	value = raw_input("Introduce definicion: ")
	diccionario[key]=value
print diccionario
	
