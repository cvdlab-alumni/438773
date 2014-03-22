
from pyplasm import *


floor0 = PROD([QUOTE([10]) , QUOTE([10])])

floor1 = T([1,2,3])([0.45,0.45,2])(S([1,2])([0.90,0.90])(floor0))

floor2 = T([1,2,3])([0.45,0.45,2])(S([1,2])([0.9,0.9])(floor1))

floor3 = T([1,2,3])([0.45,0.45,2])(S([1,2])([0.9,0.9])(floor2))

floor4 = T([1,2,3])([0.45,0.45,2])(S([1,2])([0.9,0.9])(floor3))

floor5 = T([1,2,3])([0.45,0.45,2])(S([1,2])([0.9,0.9])(floor4))

floor6 = T([1,2,3])([0.45,0.45,2])(S([1,2])([0.9,0.9])(floor5))

floors = STRUCT([floor0 , COLOR(RED)(floor1) , COLOR(YELLOW)(floor2) , COLOR(GREEN)(floor3) , 
					COLOR(ORANGE)(floor4) , COLOR(WHITE)(floor5) , COLOR(CYAN)(floor6)])

VIEW(floors)
