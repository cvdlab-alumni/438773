import sys

from simplexn import *
from larcc import *
from lar2psm import *
from largrid import *
from morph import *
from mapper import *

from pyplasm import *
from larcc import * 



#BROW1 = rgb([101,67,33])
#GREEN1 = rgb([3,192,60])

#####################################################
# Importo struttura esercizio 3
#####################################################


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
facade = COLOR([0.3, 0.4, 0.5, 0.5])(facade)

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
building1 = T([1,2])([27,34])(building1)

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
w2 = COLOR([0.3, 0.4, 0.5, 0.5])(PROD([w2 , Q(0.2)]))

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


#VIEW(building2)


#####################################################
# Creazione interni 
#####################################################

top_sedia = larPizza([0.05,1])([8,48])
top_sedia = STRUCT(MKPOLS(top_sedia))
top_sedia = T(3)(2.5)(top_sedia)

bottom_sedia = larPizza([0.02,1])([8,48])
bottom_sedia = STRUCT(MKPOLS(bottom_sedia))

asta = larRod([0.2,2.5])([32,1])
asta = STRUCT(MKPOLS(asta))  


sedia1 = STRUCT([top_sedia , bottom_sedia , asta])

tavolo = S([1,2,3])([1.5,1.5,1.5])(sedia1)
tavolo = T([1,2])([2,2])(tavolo)

sedia2 = T([1,2])([4,4])(sedia1)

tavolo_sedie = STRUCT([tavolo , sedia1 , sedia2])
tavolo_sedie = SCALE([1,2,3])([0.3,0.3,0.3])(tavolo_sedie)
tavolo_sedie = COLOR([0.803,0.521,0.247])(tavolo_sedie)

#VIEW(tavolo_sedie)

#####################################################
#####################################################

#####################################################
# Assemblamento
#####################################################

tavolo_sedie = T([1,2,3])([2,3,0.25])(tavolo_sedie)

tavolo_sedie2 = T([1,2,3])([2,-1,2.75])(tavolo_sedie)

#tavolo_sedie3 = T([1,2,3])([0.5,-1,5.75])(tavolo_sedie2)

building2 = STRUCT([building2_floors , base_b2 , top , windows_building_final , tavolo_sedie , tavolo_sedie2])
building2 = T([1,2])([5,30])(building2)
#VIEW(building2)

#####################################################
#####################################################


#####################################################
# Importo struttura principale
#####################################################

def create_floor(f):
	floors = []
	f1 = f
	floors.append(f1)
	for i in range(1,7):
		f1 = T([1,2,3])([0.5,-0.7,4])(SCALE([1,2,3])([0.9,0.9,0.9])(f1))
		floors.append(f1)
	return floors

#####################################################
# Creazione struttura
# Verranno generate le faccie verticali 
# north , sud , east , ovest 
# successivamete unite
#####################################################

face1 = CUBOID([10,2])
face1 = STRUCT([PROD([face1 , Q(4)])])

#####################################################
#Creazione finestra
#####################################################

rect = CUBOID([1,0.5])
rect = PROD([rect , Q(1.5)])
rect = T([1,2])([4.5,1.5])(rect)

arco = larRod([0.5,0.5])([32,1])
arco = R([2,3])(PI/2)(STRUCT(MKPOLS(arco)))
arco = T([1,2,3])([5,2,1.5])(arco)

window = STRUCT([rect , arco])

#####################################################
#####################################################

#VIEW(window)

faces = COLOR([0.9098, 0.5921, 0.341])(DIFFERENCE([face1 , window]))

#####################################################
# Creazione cornicione
#####################################################

points = [[0,0,3],[0,0,4],[-0.5 ,0,3.5],[10,0,3] , [10,0,4] , [10.5,0,3.5] , [10,0.5,3.5] , [0,0.5,3.5] ]
top = JOIN(AA(MK)(points))
top = COLOR([0.643 , 0.5174 , 0.376])(T(2)(2)(top))

#####################################################
#####################################################

floors_final = STRUCT([top,faces])

north = STRUCT(create_floor(floors_final))

#####################################################
# Creazione tetto della struttura
#####################################################

points_tetto = [[0,0,0] , [5.7,0,0] , [2.7,3,0] , [2.7,3,3]]
tetto = JOIN(AA(MK)(points_tetto))
tetto = R([1,2])(PI)(T([1,2,3])([-7.7,2,21])(tetto))
tetto = COLOR([0.643 , 0.5174 , 0.376])(tetto)

#####################################################
#####################################################

north = STRUCT([north , tetto])

east = T(1)(10)(ROTATE([1,2])(-PI/2)(north))
sud = T(2)(-10)(ROTATE([1,2])(PI/2)(north))
ovest = T([1,2])([-10 , -10])(ROTATE([1,2])(PI/2)(T(2)(-10)(sud)))

single_model_3D = STRUCT([north , east , sud , ovest ])

#VIEW(single_model_3D)

#####################################################
#Creazione della base della struttura
#####################################################

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

#VIEW(all_base)

#####################################################
# Creazione ringhiera
#####################################################

asta_3d = PROD([CUBOID([0.50 , 0.50]) , QUOTE([2])]) 
asta_3d = T([1,2,3])([0.5,0.5,4])(asta_3d)

pair_x1 = [T(1)(2) , asta_3d]
aste_3d_x1 = STRUCT(NN(6)(pair_x1))

pair_y = [T(2)(2) , asta_3d]
aste_3d_y1 = STRUCT(NN(6)(pair_y))

pair_x2 = [T(2)(2) , T(1)(13.5)(asta_3d)]
aste_3d_x2 = STRUCT(NN(6)(pair_x2))

aste_3d = COLOR(GRAY)(STRUCT([aste_3d_x1 , aste_3d_x2 , aste_3d_y1]))

#####################################################
#####################################################

all_base = STRUCT([all_base , aste_3d])

#VIEW(all_base)

#creazione asta orizzontale della ringhiera
a1 = CUBOID([0.5 , 14])

ring1 = COLOR(BROWN)(T([1,2,3])([0.5,0.5,5.5])(PROD([ a1, QUOTE([0.5])])))
ring2 = T(2)(1.5)(R([1,2])(-PI/2)(ring1))
ring3 = T(1)(13.5)(ring1)

struct3 = STRUCT([all_base , ring1 , ring2 , ring3] )
struct3 = SCALE([1,2,3])([1.4,1.4,1.4])(struct3)

#####################################################
#####################################################

single_model_3D = T([1,2,3])([5.5,16,6])(single_model_3D)
all_struct = STRUCT([single_model_3D , struct3])
all_struct = T([1])([24])(all_struct)

#####################################################
# Assemblamento esercizio
#####################################################

total = STRUCT([field , building1 , building2 , all_struct])

#VIEW(total)

#####################################################
# Creazione marciapiede
#####################################################

blocks = CUBOID([1,20])
blocks = PROD([blocks , Q(0.2)])
blocks = T([1,3])([0.25,0.1])(blocks)

rialzo = CUBOID([1.5,20])
rialzo = COLOR(RED)(PROD([rialzo , Q(0.3)]))

road = COLOR([0.690,0,0])(DIFFERENCE([rialzo , blocks]))

#VIEW(road)

#####################################################
#####################################################

#####################################################
# Creazione Lampione
#####################################################

palo = larRod([.05,1.2])([32,1])
palo = COLOR(GRAY)(STRUCT(MKPOLS(palo)))

torus = larTorus([0.05,0.08])()
torus = STRUCT(MKPOLS(torus))

palla = larBall(0.2)([18,36])
palla = STRUCT(MKPOLS(palla))
palla = COLOR(YELLOW)(T(3)(1.3)(palla))

lampione = STRUCT([palo , torus , T(3)(0.5)(torus) , T(3)(1)(torus) , palla])

#VIEW(lampione)

#####################################################
#####################################################

#####################################################
# Posizionamento lampioni
#####################################################

lampione = T([1,3])([0.12,0.3])(lampione)

pair_y = [T(2)(4.8) , lampione]
fila_lampioni1 = STRUCT(NN(4)(pair_y))
fila_lampioni1 = STRUCT([fila_lampioni1 , lampione])

fila_lampioni2 = T(1)(1.38)(fila_lampioni1)

fila_lampioni = STRUCT([fila_lampioni1 , fila_lampioni2])

marciapiede1 = STRUCT([fila_lampioni , road])
marciapiede1 = T([1,2])([9,5])(marciapiede1)
#VIEW(marciapiede1)

#####################################################
# Creazione secondo marciapiede
#####################################################

blocks2 = CUBOID([1,14])
blocks2 = PROD([blocks2 , Q(0.2)])
blocks2 = T([1,3])([0.25,0.1])(blocks2)

rialzo2 = CUBOID([1.5,14])
rialzo2 = COLOR(RED)(PROD([rialzo2 , Q(0.3)]))

road2 = COLOR([0.690,0,0])(DIFFERENCE([rialzo2 , blocks2]))

fila_lampioni3 = STRUCT(NN(3)(pair_y))
fila_lampioni3 = STRUCT([fila_lampioni3 , lampione])

fila_lampioni4 = T(1)(1.38)(fila_lampioni3)

fila_lampioni5 = STRUCT([fila_lampioni3 , fila_lampioni4])

marciapiede2 = STRUCT([fila_lampioni5 , road2])
marciapiede2 = T([1,2])([34,21])(marciapiede2)
#marciapiede2 = R([1,2])(-PI/2)(marciapiede2)


#####################################################
# Creazione terzo marciapiede
#####################################################

marciapiede3 = R([1,2])(-PI/2)(marciapiede2)
marciapiede3 = T([1,2])([-2,40])(marciapiede3) #-5

#####################################################
# Creazioen quarto marciapiede
#####################################################

#marciapiede4 = R([1,2])(-PI/2)(marciapiede3)
marciapiede4 = T([1,2])([1,35])(marciapiede3)

#VIEW(STRUCT([field , marciapiede3 , marciapiede4]))

#####################################################
# Creazione albero
#####################################################

tronco = larRod([.15,1])([32,1])
tronco = COLOR(GRAY)(STRUCT(MKPOLS(tronco)))
tronco = COLOR([0.396 , 0.262 , 0.129])(tronco)

chioma1 = larBall(0.2)([18,36])
chioma1 = STRUCT(MKPOLS(chioma1))

chioma1 = T(3)(1)(chioma1)

chioma = STRUCT([chioma1 , T(2)(0.5)(chioma1) , T(2)(-0.5)(chioma1) ,T(1)(0.5)(chioma1),
					T(1)(-0.5)(chioma1) , T(3)(0.5)(chioma1)])

chioma = STRUCT([R([1,2,3])(-PI/2)(chioma) , R([1,2,3])(PI/2)(chioma) , 
				R([1,2,3])(-PI/3)(chioma) , R([1,2,3])(PI/2)(chioma) ])
chioma = STRUCT([ chioma , T(3)(0.25)(chioma) ,  T(3)(0.5)(SCALE([1,2])([0.7,0.7,0.7])(chioma))])

chioma = COLOR([0.0117 , 0.752 , 0.235])(chioma)

albero = STRUCT([tronco , chioma])
albero2 = T([1,2])([15,10])(albero) # 10 10
albero3 = T([1,2])([13,41])(albero)

alberi = STRUCT([albero , albero2 , albero3])

#####################################################
# Assemblamento
#####################################################

context = STRUCT([total , marciapiede2 , marciapiede1 , marciapiede3 , marciapiede4 , alberi])
VIEW(context)








