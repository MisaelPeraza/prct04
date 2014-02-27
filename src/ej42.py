#!encoding: UTF-8
#!/usr/bin/python
#Para empezar, debemos introducir la función es_perfecto(n) corregida del ejercicio 41 ya que la vamos a llamar.

def es_perfecto(n):
  sumatorio = 0
  for i in range(1,n):
     if n%i == 0:
      sumatorio += i
  return sumatorio == n
  
def tabla_perfectos(m):
  for i in range(1, m+1):
    if es_perfecto(i):
      print i, 'es perfecto'
      
x = int(raw_input('Introduzca un número: '))
tabla_perfectos(x)

#Este programa trata de encontrar todos los números perfectos menores que el número que introduzcamos.