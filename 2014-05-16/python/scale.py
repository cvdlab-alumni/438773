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

from utilities import *


def create_stair(model):
	tensor = T([1,2,3])([0.4,0,0.3])
	steps = [model]
	step = model
	for i in range(11):
		step = tensor(step)
		steps.append(step)
	return steps


def get_stair():
	return master_stair


shape = [3,1,6]
dimension = [[0.3,9.6,0.3] , [3] , [3.5,0.4]*3]

master = assemblyDiagramInit(shape)(dimension)
#VIEW(DRAW(master))
#VIEW(DRAW_SKEL(master))


toMerge = [0]
shape = [1,3,2]
dimension = [[0.3] ,[0.5,1.8,0.5] , [2.5,1]]

door = assemblyDiagramInit(shape)(dimension)
master = inserts_in_cells(master , door  , toMerge)
toRemove = [19]
master = removes_cells(master , toRemove)

toMerge = [1]
shape = [1,3,3]
dimension = [[0.3] , [1.1,0.8,1.1] , [1.15,1.2,1.15]]

windows = assemblyDiagramInit(shape)(dimension)
master = inserts_in_cells(master , windows, toMerge)
toRemove = [25]
master = removes_cells(master , toRemove)

toMerge = [2]
master = inserts_in_cells(master , windows , toMerge)
toRemove = [32]
master = removes_cells(master , toRemove)


shape = [2,3,1]
dimension = [[7,2.6] , [0.3,2.4,0.3] , [0.4]]
floor = assemblyDiagramInit(shape)(dimension)

shape2 = [2,3,1]
dimension2 = [[2.6,7] , [0.3,2.4,0.3] , [0.4]]
floor2 = assemblyDiagramInit(shape2)(dimension2)

toMerge = [6]
master = inserts_in_cells(master , floor2 , toMerge)
toMerge = [4]
master = inserts_in_cells(master , floor , toMerge)
toRemove = [38,41]
master = removes_cells(master , toRemove)


"""Creazione scala"""
V = [[0,0] , [0,1.7] , [0.4,1.7] , [0.4,0]]
FV = [[0,1,2,3]]

model = larExtrude((V,FV) , [0.3])
stair = create_stair(STRUCT(MKPOLS(model)))
stair = STRUCT(stair)

tensor2 = T([1,2])([2.6,0]) 
tensor3 = T([2,3])([1.5,3.9]) 
tensor4 = T([2,3])([1,7.4]) 

stair = tensor2(stair)
stair2 = tensor3(stair)
stair2 = tensor4(S([3])([-1])(stair))

master_stair = STRUCT([stair, stair2  , DRAW(master)])



