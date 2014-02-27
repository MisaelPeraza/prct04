#!/usr/bin/python
#!encoding: UTF-8

a = float(raw_input('Valor de a: '))
b = float(raw_input('Valor de b: '))

if (a == 0):
  print 'Error'
else:
  x = -b/a
  print 'Solucion: ', x

#Error cuando calcula el valor de x.Añadimos la linea 7,8,9 para resolverlo.
