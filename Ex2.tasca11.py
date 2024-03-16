

from functools import reduce

m = [ 3 , 4 , 5 ]
c = list ( map ( lambda x : str ( x ), m ))
d = reduce ( lambda x , y : x + y , c )
print ( d )