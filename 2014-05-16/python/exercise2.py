""" testing initial steps of Assembly Diagram construction """
from pyplasm import *
from scipy import *
import os,sys
""" import modules from larcc/lib """
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


view_numerating_cells(master)

toMerge = 17
shape_r9 = [1,3,2]
dimesione_r9 = [[0.3] ,[1.58,0.92,1.5], [2.2,0.8]]

view_numerating_cells(master)

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


floor1 = DRAW(master)
floor2 = T([3])([3.3])(floor1)
floor3 = T([3])([3.3])(floor2)

condominio = STRUCT([floor1 , floor2 , floor3])


stair = spiralStair(nturns = 10)
stair = DRAW(stair)
stair = T([1,2])([-1,6.5])(stair)
condominio_all = STRUCT([stair , condominio])
VIEW(condominio_all)



####################################
# Costruzione base
####################################


shape = [5,5,1]
dimension = [[1,4.5,1,4.5,1] , [1,2.5,1,2.5,1] , [3]]

master_b = assemblyDiagramInit(shape)(dimension)
V,CV = master_b
hpc = SKEL_1(STRUCT(MKPOLS(master_b)))
hpc = cellNumbering (master_b,hpc)(range(len(CV)),CYAN,2)

master_b = select_elements((master_b) , [0,2,4,10,12,14,20,22,24])
hpc = DRAW(master_b)

builds = STRUCT([hpc , stair , T(3)(3)(condominio)])
#VIEW(builds)


condominio2 = T(2)(16)(condominio_all)
condominio3 = T(2)(16)(condominio2)

final_build = STRUCT([condominio_all , condominio2 , condominio3])
VIEW(final_build)

####################################
# Costruzione curve
####################################

domain = larDomain([32])
controlPoints = [[0,0,0],[.4,0,0.05],[.05,0,.25],[.2,0,.3]]
profile = BEZIER(S1)(controlPoints)
domain = EMBED(1)(PROD([ Hpc(Grid([10*[1./10]])),  Hpc(Grid([30*[2*PI/30]])) ]))
mapping = ROTATIONALSURFACE(profile)
vaso1 = COLOR(ORANGE)(MAP(mapping)(domain))
VIEW(vaso1)


domain = larDomain([48,48])
controlPoints1 = [[0,0,0],[40,0,-40],[50,0,-50]]
controlPoints2 = [[0,50.5,0],[40,50.5,20],[50,50.5,-30]]
controlPoints3 = [[0,70,0],[40,70,-10],[50,70,-30]]

b1 = BEZIER(S1)(controlPoints1)
b2 = BEZIER(S1)(controlPoints2)
b3 = BEZIER(S1)(controlPoints3)

mapping = BEZIER(S2)([b1,b2,b3])
surface = larMap(mapping)(domain)
model = STRUCT(MKPOLS(surface))
VIEW(model)



