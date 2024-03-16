def resumen_python():
    opcion = 0
    while opcion<1 or opcion>5:
        print ("""Selecciona que apartado quieres:
               1. Programación estructurada
               2. P. Funcional
               3. P.O.O
               4. Accesos a Ficheros
               5. Salir
           """)
        opcion = int(input("Escoje la opción con números del 1 al 5: "))
        if opcion<1 or opcion>5:
            print("Opció no vàlida")
        else:
            return opcion 



def Programación_estructurada():
    print("Muy estructural, no?")

def Programación_Funcional():
    print("La tienes Funcional?")

def Programación_orientado_objetos():
    print("P.O.O selected")

def Accesos_Ficheros():
    print("Entraste")


#PP   
op=1
while op!=5:
    op=resumen_python()
    match(op):
        case 1:
            Programación_estructurada()
        case 2:
            Programación_Funcional()
        case 3:
            Programación_orientado_objetos()
        case 4:
            Accesos_Ficheros()
        case 5:
            print("ADIOS")
        case other:
            print("Opció no vàlida! ")

    