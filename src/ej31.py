#!/usr/bin/python
#!encoding: UTF-8

numero = int( raw_input('Introduzca un numero: '))

for potencia in [2,3,4,5]:
  print '%d elevado a %d es %d' % (numero, potencia, numero**potencia)
  
#Imprime en la consola el número que hemos introducido al cuadrado, al cubo, a la cuarta y a la quinta. 