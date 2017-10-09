lista = [5,3.5,4,2.5]

suma = 0
n = len(lista)
for i in lista:
    suma += i
media = suma/n
print (media)
    
suma2 = 0    
for i in lista:
    suma2+= (i-media)**2
varianza  = suma2/(n-1)
print (varianza)
