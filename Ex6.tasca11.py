def coincideixen(llista):
    l=[]
    for i,e in enumerate (llista):
        if e == i:
            l.append(e)
    print("Els elements de la llista {} que concideixen en la seva posició són {}".format(llista,llista))
          
#Programa principal. Ex6
l=[3,7,2,3,4,5,6,7,8,9,10,1]
coincideixen(l)