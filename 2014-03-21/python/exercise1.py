
from pyplasm import *

wall0 = PROD([QUOTE([10]) , QUOTE([10])])
internal0 = T([1,2])([0.5,0.5])(PROD([QUOTE([9]) , QUOTE([9])]))
floor0 = STRUCT([wall0 , COLOR(BROWN)(internal0)])

wall1 = T([1,2,3])([0.45,0.45,2])(S([1,2])([0.90,0.90])(wall0))
internal1 = T([1,2,3])([0.45,0.45,2])(S([1,2])([0.90,0.90])(internal0))
floor1 = STRUCT([wall1 , COLOR(RED)(internal1)])

wall2 = T([1,2,3])([0.45,0.45,2])(S([1,2])([0.9,0.9])(wall1))
internal2 = T([1,2,3])([0.45,0.45,2])(S([1,2])([0.90,0.90])(internal1))
floor2 = STRUCT([wall2 , COLOR(YELLOW)(internal2)])

wall3 = T([1,2,3])([0.45,0.45,2])(S([1,2])([0.9,0.9])(wall2))
internal3 = T([1,2,3])([0.45,0.45,2])(S([1,2])([0.90,0.90])(internal2))
floor3 = STRUCT([wall3 , COLOR(GREEN)(internal3)])

wall4 = T([1,2,3])([0.45,0.45,2])(S([1,2])([0.9,0.9])(wall3))
internal4 = T([1,2,3])([0.45,0.45,2])(S([1,2])([0.90,0.90])(internal3))
floor4 = STRUCT([wall4 , COLOR(ORANGE)(internal4)])

wall5 = T([1,2,3])([0.45,0.45,2])(S([1,2])([0.9,0.9])(wall4))
internal5 = T([1,2,3])([0.45,0.45,2])(S([1,2])([0.90,0.90])(internal4))
floor5 = STRUCT([wall5 , COLOR(BLACK)(internal5)])

wall6 = T([1,2,3])([0.45,0.45,2])(S([1,2])([0.9,0.9])(wall5))
internal6 = T([1,2,3])([0.45,0.45,2])(S([1,2])([0.90,0.90])(internal5))
floor6 = STRUCT([wall6 , COLOR(CYAN)(internal6)])

floors = STRUCT([floor0 , floor1 , floor2 , floor3 , floor4 , floor5 , floor6])

VIEW(floors)

