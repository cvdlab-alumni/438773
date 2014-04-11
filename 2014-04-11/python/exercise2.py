import sys

from simplexn import *
from larcc import *
from lar2psm import *
from largrid import *
from morph import *
from mapper import *

from pyplasm import *
from larcc import * 


def create_floor(f):
	floors = []
	f1 = f
	floors.append(f1)
	for i in range(1,7):
		f1 = T([1,2,3])([0.5,-0.7,4])(SCALE([1,2,3])([0.9,0.9,0.9])(f1))
		floors.append(f1)
	return floors


face1 = CUBOID([10,2])
face1 = STRUCT([PROD([face1 , Q(4)])])

#Create Window
rect = CUBOID([1,0.5])
rect = PROD([rect , Q(1.5)])
rect = T([1,2])([4.5,1.5])(rect)

arco = larRod([0.5,0.5])([32,1])
arco = R([2,3])(PI/2)(STRUCT(MKPOLS(arco)))
arco = T([1,2,3])([5,2,1.5])(arco)

window = STRUCT([rect , arco])

#VIEW(window)

faces = COLOR([0.9098, 0.5921, 0.341])(DIFFERENCE([face1 , window]))

points = [[0,0,3],[0,0,4],[-0.5 ,0,3.5],[10,0,3] , [10,0,4] , [10.5,0,3.5] , [10,0.5,3.5] , [0,0.5,3.5] ]
top = JOIN(AA(MK)(points))
top = COLOR([0.643 , 0.5174 , 0.376])(T(2)(2)(top))

floors_final = STRUCT([top,faces])

north = STRUCT(create_floor(floors_final))


#VIEW(single_model)

points_tetto = [[0,0,0] , [5.7,0,0] , [2.7,3,0] , [2.7,3,3]]
tetto = JOIN(AA(MK)(points_tetto))
tetto = R([1,2])(PI)(T([1,2,3])([-7.7,2,21])(tetto))
tetto = COLOR([0.643 , 0.5174 , 0.376])(tetto)

north = STRUCT([north , tetto])

east = T(1)(10)(ROTATE([1,2])(-PI/2)(north))
sud = T(2)(-10)(ROTATE([1,2])(PI/2)(north))
ovest = T([1,2])([-10 , -10])(ROTATE([1,2])(PI/2)(T(2)(-10)(sud)))

#north = T(1)(3)(S(1)(1.3)(north))
single_model_3D = STRUCT([north , east , sud , ovest ])

#VIEW(single_model_3D)

#####################################################
#Crete base
major_base = CUBOID([15,15])

minor_base = T([1,2,3])([0.5,0.5,4])(CUBOID([14,14]))

S = AA(JOIN)([major_base , minor_base])
base = JOIN(S)

#VIEW(base)

trasl = T([1,2,3])([0.7,0.7,4])
p = PROD([QUOTE([0.5,-13,0.5]) , QUOTE([0.5,-13,0.5])])
p2 = COLOR(BROWN)(PROD([p , QUOTE([2])]))

pali = T([1,2,3])([0.5,0.5,4])(p2)

all_base = STRUCT([base , pali])

#VIEW(all)

#creazione pali ringhiera
asta_3d = PROD([CUBOID([0.50 , 0.50]) , QUOTE([2])]) 
asta_3d = T([1,2,3])([0.5,0.5,4])(asta_3d)

pair_x1 = [T(1)(2) , asta_3d]
aste_3d_x1 = STRUCT(NN(6)(pair_x1))

pair_y = [T(2)(2) , asta_3d]
aste_3d_y1 = STRUCT(NN(6)(pair_y))

pair_x2 = [T(2)(2) , T(1)(13.5)(asta_3d)]
aste_3d_x2 = STRUCT(NN(6)(pair_x2))

aste_3d = COLOR(GRAY)(STRUCT([aste_3d_x1 , aste_3d_x2 , aste_3d_y1]))

all_base = STRUCT([all_base , aste_3d])

#VIEW(all_base)

#creazione asta orizzontale della ringhiera
a1 = CUBOID([0.5 , 14])

ring1 = COLOR(BROWN)(T([1,2,3])([0.5,0.5,5.5])(PROD([ a1, QUOTE([0.5])])))
ring2 = T(2)(1.5)(R([1,2])(-PI/2)(ring1))
ring3 = T(1)(13.5)(ring1)

struct3 = STRUCT([all_base , ring1 , ring2 , ring3] )
struct3 = SCALE([1,2,3])([1.4,1.4,1.4])(struct3)

############################################

single_model_3D = T([1,2,3])([5.5,16,6])(single_model_3D)
all_struct = STRUCT([single_model_3D , struct3])
VIEW(all_struct)




