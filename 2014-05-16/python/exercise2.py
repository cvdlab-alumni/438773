from pyplasm import *
from scipy import *
import os,sys

from lar2psm import *
from simplexn import *
from larcc import *
from largrid import *
from mapper import *
from boolean import *

from sysml import *
from splines import *
from architectural import *



def removes_elements((V,CV) , indices_remove):
	return V,[cell for k,cell in enumerate(CV) if not (k in indices_remove)]
	
def select_elements((V,CV) , indices):
	return V,[cell for k,cell in enumerate(CV) if (k in indices)]

def view_numerating_cells(master):
	hpc = SKEL_1(STRUCT(MKPOLS(master)))
	hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
	VIEW(hpc)

def inserts_elements(master , diagram , cells):
	cells.sort(reverse=True)
	for i,item in enumerate(cells):
		master = diagram2cell(diagram , master , item)
	return master

DRAW = COMP([STRUCT,MKPOLS])
DRAW_SKEL = COMP([SKEL_1,STRUCT,MKPOLS])

shape = [3,3,2]
dimension = [[.3,12,.3],[.3,12,.3],[.4,3]]


master = assemblyDiagramInit(shape)(dimension)
V,CV = master
block1 = DRAW_SKEL(master)

appartament = cellNumbering(master,block1)(range(len(CV)),RED,2)
#VIEW(appartament)


######################
# Prima camera
######################

toMerge = 9
shape_r1 = [3,3,1]
dimesione_r1 = [[7,0.3,7] , [6,0.3,4] , [3]]

#view_numerating_cells(master)

cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([appartament,cell]))

room1 = assemblyDiagramInit(shape_r1)(dimesione_r1)
master = diagram2cell(room1 , master , toMerge)
block2 = DRAW_SKEL(master)
block2 = cellNumbering(master,block2)(range(len(master[1])),CYAN,2)

#VIEW(block2)

toRemove = [23]
master = removes_elements(master , toRemove)
#VIEW(DRAW(master))


######################
# Seconda camera
######################

toMerge = 17
shape_r2 = [1,3,1]
dimesione_r2 = [[5] , [4,0.3,2] , [3]]

#view_numerating_cells(master)

cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([appartament,cell]))

room2 = assemblyDiagramInit(shape_r2)(dimesione_r2)
master = diagram2cell(room2 , master , toMerge)
block3 = DRAW_SKEL(master)
block3 = cellNumbering(master,block3)(range(len(master[1])),CYAN,2)

#VIEW(block3)

toRemove = [24]
master = removes_elements(master , toRemove)
#VIEW(DRAW(master))



######################
# Terza camera
######################

toRemove = [25]
master = removes_elements(master , toRemove)
#VIEW(DRAW(master))

######################
# Quarta camera
######################

toRemove = [18]
master = removes_elements(master , toRemove)
#VIEW(DRAW(master))


######################
# Quinta camera
######################

toMerge = 22
shape_r5 = [3,1,1]
dimesione_r5 = [[2,0.3,5] ,[4], [3]]

#view_numerating_cells(master)

cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([appartament,cell]))

room5 = assemblyDiagramInit(shape_r5)(dimesione_r5)
master = diagram2cell(room5 , master , toMerge)
block4 = DRAW_SKEL(master)
block4 = cellNumbering(master,block4)(range(len(master[1])),CYAN,2)

#VIEW(block4)

toRemove = [25]
master = removes_elements(master , toRemove)
#VIEW(DRAW(master))

######################
# Sesta camera
######################

toRemove = [23]
master = removes_elements(master , toRemove)
#VIEW(DRAW(master))


########################
# Costruzione finestre
# con suddivisione pareti
########################

toMerge = 14
shape_r6 = [1,10,3]
dimesione_r6 = [[0.3] ,[1.2,1.30,0.1,0.85,1.95,0.9,0.85,0.1,1.2,0.9], [0.9,1.3,0.7]]

#view_numerating_cells(master)

cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([appartament,cell]))

wall1 = assemblyDiagramInit(shape_r6)(dimesione_r6)
master = diagram2cell(wall1 , master , toMerge)
block5 = DRAW_SKEL(master)
block5 = cellNumbering(master,block5)(range(len(master[1])),CYAN,2)

#VIEW(block5)

toRemove = [27,32,33,41,42,48]
master = removes_elements(master , toRemove)
#VIEW(DRAW(master))


########################
# 
#
########################

toMerge = 3
shape_r7 = [1,11,3]
dimesione_r7 = [[0.3] ,[1.4,1.2,1.4,0.7,0.6,0.7,0.9,0.85,0.1,1.2,0.9], [0.9,1.3,0.7]]

#view_numerating_cells(master)

cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([appartament,cell]))

wall2 = assemblyDiagramInit(shape_r7)(dimesione_r7)
master = diagram2cell(wall2 , master , toMerge)
block6 = DRAW_SKEL(master)
block6 = cellNumbering(master,block6)(range(len(master[1])),CYAN,2)

#VIEW(block6)

toRemove = [50,59,67,68,74]
master = removes_elements(master , toRemove)
#VIEW(DRAW(master))



########################
# Costruzione porte
#
########################


toMerge = 16
shape_r8 = [1,7,2]
dimesione_r8 = [[0.3] ,[1.54,0.92,1.54,0.3,0.54,0.92,0.54], [2.2,0.8]]

#view_numerating_cells(master)

cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([appartament,cell]))

wall3 = assemblyDiagramInit(shape_r8)(dimesione_r8)
master = diagram2cell(wall3 , master , toMerge)
block7 = DRAW_SKEL(master)
block7 = cellNumbering(master,block7)(range(len(master[1])),CYAN,2)

#VIEW(block7)

toRemove = [75,83]
master = removes_elements(master , toRemove)
#VIEW(DRAW(master))

########################
########################
########################

toMerge = 17
shape_r9 = [1,3,2]
dimesione_r9 = [[0.3] ,[1.58,0.92,1.5], [2.2,0.8]]

#view_numerating_cells(master)

cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([appartament,cell]))

wall4 = assemblyDiagramInit(shape_r9)(dimesione_r9)
master = diagram2cell(wall4 , master , toMerge)
block8 = DRAW_SKEL(master)
block8 = cellNumbering(master,block8)(range(len(master[1])),CYAN,2)

#VIEW(block8)

toRemove = [86]
master = removes_elements(master , toRemove)
#VIEW(DRAW(master))

########################
########################
########################


toMerge = 17
shape_r10 = [6,1,2]
dimesione_r10 = [[0.54,0.92,0.54,0.3,3,2] , [0.3] , [2.2,0.8]]

#view_numerating_cells(master)

cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
#VIEW(STRUCT([appartament,cell]))

wall5 = assemblyDiagramInit(shape_r10)(dimesione_r10)
master = diagram2cell(wall5 , master , toMerge)
block9 = DRAW_SKEL(master)
block9 = cellNumbering(master,block9)(range(len(master[1])),CYAN,2)

#VIEW(block9)

toRemove = [90, 98]
master = removes_elements(master , toRemove)
#VIEW(DRAW(master))



####################################
# Esercizio 2
####################################



#####################
# Inserimento piani
#####################

master_condominio = assemblyDiagramInit([3,1,1])([[12.3,3,12.3] , [10] , [17.6]])
VIEW(DRAW_SKEL(master_condominio))

condominio_p1 = assemblyDiagramInit([1,1,8])([[12.3],[10],[4,0.4]*4])
master_condominio = inserts_elements(master_condominio , condominio_p1 , [0,2])

VIEW(DRAW_SKEL(master_condominio))

####################################
# Costruzione base
####################################

shape = [3,1,1]
dimension = [[1.5,9,1.5] , [10] , [4]]

master_b = assemblyDiagramInit(shape)(dimension)
condominio = inserts_elements(master_b,condominio,[0])
condominio = removes_elements(condominio , [299])
#VIEW(DRAW(condominio))


condominio = STRUCT([ T([2])([12])(DRAW(condominio)) , DRAW(condominio)])
#VIEW(condominio)

####################################
# Costruzione curve
####################################

controls = [[2,0,0] , [2,0,1] , [3,0,2] , [4,0,3]]
controls1 = [[4,0,3] , [5,0,2] , [6,0,1] , [6,0,0]]
#controls2 = [[1,0,0] , [1,0,0] , [2,0,1] , [3,0,2]]
#controls3 = [[3,0,2] , [4,0,1] , [5,0,0] , [5,0,0]]

b1 = BEZIER(S1)(controls)
b2 = BEZIER(S1)(controls1)

domain = larDomain([48,48])
mapping2 = BEZIER(S2)([b1,b2])
surface2 = larMap(mapping2)(domain)
surface_curva = COLOR(RED)(STRUCT(MKPOLS(surface2)))
#VIEW(surface_curva)


#condominio = STRUCT([condominio , surface_curva])
#VIEW(condominio)


"""Costruzione Vaso"""

def rotationalSurface2(profile):
	domain = EMBED(1)(PROD([ Hpc(Grid([10*[1./10]])),  Hpc(Grid([30*[2*PI/30]])) ]))
	mapping = ROTATIONALSURFACE(profile)
	obj = MAP(mapping)(domain)
	return obj

def create_profile(controlPoints):
	b1 = BEZIER(S1)(controlPoints[0])
	b2 = BEZIER(S1)(controlPoints[1])
	profile = BEZIER(S1)([b1,b2])
	return profile

domain = larDomain([32])
controlPoints = [[[0.5, 0.0, 0.0], [0.25, 0.0, 0.0], [0.25, 0.0, 0.25]], [[0.25, 0.0, 0.25], [0.25, 0.0, 0.75], [0.5, 0.0, 0.75]], [[0.5, 0.0, 0.75], [0.5, 0.0, 1.0], [0.75, 0.0, 1.0]]]

profile = create_profile(controlPoints)
obj2 = rotationalSurface2(profile)

vaso1 = COLOR(RED)(obj2)
vaso2 = COLOR(RED)(T([1,2])([9,9])(vaso1))
vaso3 = COLOR(RED)(T([1,2])([3,9])(vaso1))

terreno = COLOR(GREEN)(CUBOID([30,30]))

condominio = COLOR([0.82,0.70,0.54])(STRUCT([condominio]))
condominio = STRUCT([condominio , vaso2 , vaso3 , terreno])


"""Vaso 2"""

controlPoints = [[0,0,0],[2,0,0.5],[.5,0,1.5],[2,0,2]]
profile = BEZIER(S1)(controlPoints)
obj3 = rotationalSurface2(profile)

vaso4 = COLOR(ORANGE)(T([1,2])([4,4])(obj3))
condominio = STRUCT([condominio , vaso2 , vaso3 , vaso4 , terreno])

#VIEW(condominio)


