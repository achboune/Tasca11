def lenp ( frase ):
    b = frase.split( " " )
    c = list ( map ( len , b ))
    print ( "La frase {} té la següent longitud {} " . format ( frase , c ))

a = "És una frase on treballem"
lenp ( a )