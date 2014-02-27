#!encoding: UTF-8
#!/usr/bin/python

a= ['gato', 'ventana', 'defenestrado']
for x in a:
    print x, len(x)
#Imprime gato 4 ventana 7 defenestrado 1


for x in a[:]:
  if len(x) > 6: 
    a.insert(0,x)
    print a
    
#Imprime ['ventana', 'gato', 'ventana', 'defenestrado']
#['defenestrado', 'ventana', 'gato', 'ventana', 'defenestrado']
