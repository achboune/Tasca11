def filter_words(llista, c):
    f = filter (lambda x: x[0]==c, llista)
    print("De la llista {}, las palabras por {} son {}".format(llista ,c ,list(f)))

#pp+
llista= ["Josep", "Joan", "Jordi", "Maria", "Marc", "Pere", "Paula"]
c= "J"
filter_words(llista,c)


