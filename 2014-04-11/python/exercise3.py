import sys

from simplexn import *
from larcc import *
from lar2psm import *
from largrid import *
from morph import *
from mapper import *

from pyplasm import *
from larcc import * 


def face2edge(FV):
	edges = AA(sorted)(CAT([TRANS([face[:-1] ,face[1:]]) for face in FV ])) 
	edges = AA(str)(edges) #converto in stringa cosi' il set che faro' potra' fare l'hash ed eliminare i duplicati
	edges = AA(eval)(set(edges))
	return edges

field = COLOR([0.164,0.37,0.168])(CUBOID([50,50]))

#####################################################
# Creazione base edificio 1
# base_b1 = base building 1
# base_bx = base building x
#####################################################

base1 = CUBOID([14,14])
base1 = PROD([base1 , QUOTE([0.5])])

base2 = CUBOID([13,13])
base2 = T([1,2])([0.5,0.5])(PROD([base2 , QUOTE([1])]))

base_b1 = COLOR(GRAY)(STRUCT([base1,base2]))

#####################################################
# Creazione colonne edificio 1
#####################################################

fondamenta = PROD([QUOTE([-1,1,-2,1,-2,1,-2,1,-1]) , QUOTE([-1,1,-2,1,-2,1,-2,1,-1])])
fondamenta = PROD([fondamenta , Q(3)])
fondamenta = COLOR(WHITE)(T([1,2,3])([1,1,1])(fondamenta))

base_final = STRUCT([base_b1 , fondamenta])

#####################################################
# Creazione piani edificio 1
#####################################################

V = [[0,0] , [3,0] , [10,0] , [10,3] , [3,3] , [10,10] , [3,10] , [0,10]]
FV = [[0,1,4,6,7,0] , [4,3,5,6,4] , [1,2,3,4,1]]

hpc = MKPOLS((V,FV))

poly = STRUCT(AA(POLYLINE)([ [ V[v] for v in cell ] for cell in FV]))

#Creazione spigoli
EV = face2edge(FV)
#VIEW(STRUCT(MKPOLS((V,EV))))

modelEdges = (V,EV)
modelFaces = (V,FV)

V0 = AA(LIST)([0.,3.,6.])
C0V = AA(LIST)(range(3)) 
C1V = [[0,1],[1,2]]

modelFloor = V0, C0V
modelWall = V0,C1V

mod2D = larModelProduct([modelFaces , modelFloor])
mod1D = larModelProduct([modelEdges , modelFloor])
modWall1D = larModelProduct([modelEdges , modelWall])

structure_building = STRUCT(AA(COLOR(GRAY))(MKPOLS((mod1D))) + MKPOLS((mod2D)) + MKPOLS((modWall1D)))
structure_building = COLOR([0.333 , 0.333 , 0.345])(structure_building)
#building1 = ([1,2])([30,30])(STRUCT([base_b1 , field]))
#building1 = STRUCT([fondamenta , base_b1, field])
#VIEW(building1)

#####################################################
# Crezione facciata edificio
#####################################################

v1, c1 = [[0.],[1.],[2.],[3.]],[[0,1],[1,2],[2,3]]
v0, c0 = [[0.],[1.],[2.]], [[0],[1],[2]]

vertGrid = larVertProd([v1, v1])
cellGrid = larCellProd([c1, c1])
grid3D = vertGrid,cellGrid

facade = EXPLODE(1.4,1.4,1.4)(MKPOLS(grid3D))
#facade = PROD([QUOTE([1]) , facade])
facade = R([1,3])(PI/2)(facade)
facade = S([2,3])([2.4,1.4])(facade)
facade = T(2)(0.0001)(facade)
facade = COLOR(WHITE)(facade)

facade_2 = R([1,2])(-PI/2)(facade)
facade_3 = T(2)(10)(facade_2)
facade_4 = T(1)(10)(facade)

#####################################################
#####################################################

#####################################################
# Assemblamento edificio 1
#####################################################

structure_building = STRUCT([structure_building ,facade , facade_2 , facade_3 , facade_4])
#structure_building = DIFFERENCE([facade_2 , structure_building])
#structure_building = DIFFERENCE([facade_3 , structure_building])
#structure_building = DIFFERENCE([facade_4 , structure_building])

structure_building = T([1,2,3])([2,2,4])(structure_building)

building1 = STRUCT([structure_building , base_final])

VIEW(building1)

#####################################################
# Creazione edificio 2
#####################################################












