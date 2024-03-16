def imprimir_fitxer(m):
    a =  []
    with open(m, "r") as f:
        for e in f:
            c = e.split("\n")
            if c!="":
                a.append(c[0])
    print(a)

def afegir_fitxer(m,llista):
    with open(m,"a+") as f:
        for e in llista:
            f.writelines(e)


#Program pricipal 
fitxer = "/home/cicles/AO/Tasca11/ex11.txt"
llista= ["Jordi, Ayoub, David, Oscar, Joan"]
imprimir_fitxer(fitxer)
afegir_fitxer(fitxer, llista)