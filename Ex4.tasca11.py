def ajuntar(l,d,c):
    a= []
    for i in range(len(l)):
            a.append(l[i]+c+d[i])
    print("La union de las {} y {} es {}".format(l,d,a))

#programa
l = ["Super", "Hiper", "Mini", "Maxi"]
d = ["Women", "bole", "Mouse", "Boom"]
ajuntar(l,d,"-")