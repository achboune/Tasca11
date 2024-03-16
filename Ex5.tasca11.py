def crear_diccionari(llista):
    dic={}
    for i,e in enumerate(llista):
        dic[e]= i   
    print("De la llista {} hem creat el diccionari {}".format(llista,dic))

#Programa principal. Ex5 de la tasca 11
llista=["Cotxe", "Casa", "Vaixell", "Colom", "Ca", "Mussol", "Clara"]
crear_diccionari(llista)

