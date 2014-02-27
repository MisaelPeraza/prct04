#!encoding: UTF-8
#!/usr/bin/python

def es_perfecto(n):
  for i in range(1,n):
    sumatorio = 0
    if n%i == 0:
      sumatorio += i
    return sumatrio == n

#El error de esta función es en la línea 6 ya que éste debería ir fuera del for. Al estar dentro cada vez que avanza un i y se haya almacenado en sumatorio éste se inicializa a 0.