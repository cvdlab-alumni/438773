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
#
# Vedere in /images/fig0.png il modello di riferimento
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
#VIEW(structure_building)

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
building1 = T([1,2])([30,30])(building1)

#VIEW(building1)

#####################################################
# Creazione edificio 2
# Vedere in /images/fig1.png il modello di riferimento
#####################################################

#####################################################
# Creazione base
#####################################################

base1_b2 = CUBOID([8,6])
base2_b2 = CUBOID([7.5,5.5])

base2_b2 = T([1,2])([0.25,0.25])(PROD([base2_b2 , Q(0.25)]))
base2_b2 = COLOR(WHITE)(base2_b2)

#base_b2 = STRUCT([base2_b2 , base1_b2])

colonna = larRod([.1,2.5])([32,1])
colonna = STRUCT(MKPOLS(colonna))
colonna = T([1,2,3])([1,1,0.25])(colonna)

colonna2 = T(2)(4)(colonna)
colonna3 = T(1)(6)(colonna)
colonna4 = T(2)(4)(colonna3)

base_b2 = STRUCT([base2_b2 , base1_b2 , colonna , colonna2 , colonna3 , colonna4])
#VIEW(base_b2)


#####################################################
#####################################################

#####################################################
# Creazione piani
# viene creato il primo piano e poi replicato
#####################################################


def create_bulding_floors(floor):
	floors = []
	f1 = floor
	for i in range(1,3):
		f1 = T(3)(2.75)(f1)
		floors.append(f1)
	return floors



f1 = CUBOID([8,6])
f1 = COLOR(BLACK)(PROD([f1 , Q(0.2)]))

f_int = CUBOID([7,5])
f_int = T([1,2])([0.25,0.25])(PROD([f_int , Q(1.5)]))

f_ext = CUBOID([7.5,5.5])
f_ext = PROD([f_ext , Q(1.5)])

f_t = COLOR(WHITE)(T([1,2])([0.25,0.25])(DIFFERENCE([f_ext , f_int])))

colonne = STRUCT([colonna,colonna3,colonna2,colonna4])

floor = STRUCT([f1 , f_t , colonne])

building2_floors = STRUCT(create_bulding_floors(floor))

#VIEW(building_floors)


#####################################################
# Creazione finestre
#####################################################

w1 = CUBOID([1,1.25])
w2 = CUBOID([0.9,1.15])

w1 = COLOR(GRAY)(PROD([w1 , Q(0.2)]))
w2 = T([1,2])([0.05,0.05])(w2)
w2 = COLOR(WHITE)(PROD([w2 , Q(0.2)]))

window =  STRUCT([w1 , w2])
window = R([2,3])(PI/2)(window)

windows = STRUCT([window , T(1)(1)(window)])
#VIEW(windows)

#####################################################
#####################################################


#####################################################
# Creazione tetto
#####################################################

top = SCALE(3)(0.7)(STRUCT([f_t ,f1]))
top = T(3)(8.25)(top)

#####################################################
# Assemblamento edificio
#####################################################

windows = T([1,2,3])([1.2,0.45,4.25])(windows)

pair_x = [T(1)(2) , windows]
windows_final_1 = STRUCT(NN(2)(pair_x))

windows_final_2 = T([1,3])([-1,2.75])(windows_final_1)
windows_final_3 = T(2)([5.25])(windows_final_2)
windows_final_4 = T(2)([5.25])(windows_final_1)

windows_final_5 = T(1)(0.75)(R([1,2])(PI/2)(windows))
windows_final_6 = T([2,3])([1,2.75])((windows_final_5))

windows_building_final = STRUCT([windows_final_1 , windows_final_2 , windows_final_3 , windows_final_4 , windows_final_5,
								windows_final_6])

building2 = STRUCT([building2_floors , base_b2 , top , windows_building_final])

VIEW(building2)








