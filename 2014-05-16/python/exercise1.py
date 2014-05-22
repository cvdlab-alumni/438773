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

from utilities import *


def removes_elements((V,CV) , indices_remove):
	return V,[cell for k,cell in enumerate(CV) if not (k in indices_remove)]

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
VIEW(appartament)


######################
# Prima camera
######################

toMerge = 9
shape_r1 = [3,3,1]
dimesione_r1 = [[7,0.3,7] , [6,0.3,4] , [3]]

cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
VIEW(STRUCT([appartament,cell]))

room1 = assemblyDiagramInit(shape_r1)(dimesione_r1)
master = diagram2cell(room1 , master , toMerge)

VIEW(DRAW_SKEL(master))

toRemove = [23]
master = removes_elements(master , toRemove)
VIEW(DRAW(master))

######################
# Seconda camera
######################

toMerge = 17
shape_r2 = [1,3,1]
dimesione_r2 = [[5] , [4,0.3,2] , [3]]

#view_numerating_cells(master)

cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
VIEW(STRUCT([appartament,cell]))

room2 = assemblyDiagramInit(shape_r2)(dimesione_r2)
master = diagram2cell(room2 , master , toMerge)

VIEW(DRAW_SKEL(master))

toRemove = [24]
master = removes_elements(master , toRemove)
VIEW(DRAW(master))


######################
# Terza camera
######################

toRemove = [25]
master = removes_elements(master , toRemove)
VIEW(DRAW(master))

######################
# Quarta camera
######################


toRemove = [18]
master = removes_elements(master , toRemove)
VIEW(DRAW(master))


######################
# Quinta camera
######################

toMerge = 22
shape_r5 = [3,1,1]
dimesione_r5 = [[2,0.3,5] ,[4], [3]]

view_numerating_cells(master)

cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
VIEW(STRUCT([appartament,cell]))

room5 = assemblyDiagramInit(shape_r5)(dimesione_r5)
master = diagram2cell(room5 , master , toMerge)

VIEW(DRAW(master))

toRemove = [25]
master = removes_elements(master , toRemove)
VIEW(DRAW(master))

######################
# Sesta camera
######################

toRemove = [23]
master = removes_elements(master , toRemove)
VIEW(DRAW(master))


########################
# Costruzione finestre
# con suddivisione pareti
########################


view_numerating_cells(master)

toMerge = 14
shape_r6 = [1,10,3]
dimesione_r6 = [[0.3] ,[1.2,1.30,0.1,0.85,1.95,0.9,0.85,0.1,1.2,0.9], [0.9,1.3,0.7]]

view_numerating_cells(master)

cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
VIEW(STRUCT([appartament,cell]))

wall1 = assemblyDiagramInit(shape_r6)(dimesione_r6)
master = diagram2cell(wall1 , master , toMerge)
block5 = DRAW_SKEL(master)
block5 = cellNumbering(master,block5)(range(len(master[1])),CYAN,2)

VIEW(block5)


########################
# 
#
########################


view_numerating_cells(master)

toMerge = 3
shape_r7 = [1,11,3]
dimesione_r7 = [[0.3] ,[1.4,1.2,1.4,0.7,0.6,0.7,0.9,0.85,0.1,1.2,0.9], [0.9,1.3,0.7]]

view_numerating_cells(master)

cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
VIEW(STRUCT([appartament,cell]))

wall2 = assemblyDiagramInit(shape_r7)(dimesione_r7)
master = diagram2cell(wall2 , master , toMerge)

VIEW(DRAW_SKEL(master))


########################
# Costruzione porte
#
########################

view_numerating_cells(master)

toMerge = 16
shape_r8 = [1,7,2]
dimesione_r8 = [[0.3] ,[1.54,0.92,1.54,0.3,0.54,0.92,0.54], [2.2,0.8]]

view_numerating_cells(master)

cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
VIEW(STRUCT([appartament,cell]))

wall3 = assemblyDiagramInit(shape_r8)(dimesione_r8)
master = diagram2cell(wall3 , master , toMerge)

VIEW(DRAW_SKEL(master))


########################
########################
########################


view_numerating_cells(master)

toMerge = 17
shape_r9 = [1,3,2]
dimesione_r9 = [[0.3] ,[1.58,0.92,1.5], [2.2,0.8]]

view_numerating_cells(master)

cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
VIEW(STRUCT([appartament,cell]))

wall4 = assemblyDiagramInit(shape_r9)(dimesione_r9)
master = diagram2cell(wall4 , master , toMerge)

VIEW(DRAW_SKEL(master))

########################
########################
########################


toMerge = 17
shape_r10 = [6,1,2]
dimesione_r10 = [[0.54,0.92,0.54,0.3,3,2] , [0.3] , [2.2,0.8]]

view_numerating_cells(master)

cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
VIEW(STRUCT([appartament,cell]))

wall5 = assemblyDiagramInit(shape_r10)(dimesione_r10)
master = diagram2cell(wall5 , master , toMerge)

VIEW(DRAW_SKEL(master))


windowsChain = [50,59,67,68,74,27,32,33,41,42,48]
doorChain = [75,83,90,86] # 98 --> porta cucina ? 





