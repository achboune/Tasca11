from functools import reduce 
#Añade la B a las palabras

lista = ["Pedro", "Pepe", "Leiner", "David,", "Oscar"]
m = list(map(lambda x: x+b"", lista))
print(m)


#Filtra las palabras con más de 4 letras 
lista = ["Pedro", "Pepe", "Leiner", "David,", "Oscar"]
m = list(filter(lambda x: len(x)>4, lista))
print(m)

#Suma elementos acumulado de la lista con el siguiente, con reduce 

# Suma element acumulat de la llista amb el següent, amb reduir
 
n = [1,2,3,4,5]
f = ["Hola", "Soy", "Leiner"]
print (n)
print (f)
suma = reduir(lambda a, b: a+b, n)
print (suma)
juntar = reduir(lambda q, w: q+w, f)
print (juntar)
 
 # Zip
 
y = ["Super", "Ultra", "Consumo", "Mickie", "SuperMega"]
e = ["Dona", "Bucle", "Crack", "Ratolí", "Pirilu"]
f = list(zip(y,e))
print (f)
