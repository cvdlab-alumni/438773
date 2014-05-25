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
from exercise1 import *
from scale import *


def TREE():
	tronco = COLOR([0.396 , 0.262 , 0.129])(CYLINDER([0.20,2.5])(25))
	chioma = T(3)(1.4+2.5)(COLOR([0.0117 , 0.752 , 0.235])(SPHERE(1.4)([16,16])))
	chioma2 = T(3)(2.4+2.5)(COLOR([0.0117 , 0.752 , 0.235])(SPHERE(1)([10,10])))
	return STRUCT([tronco , chioma2 , chioma])

#####################
# Inserimento piani
#####################

master_condominio = assemblyDiagramInit([1,3,1])([[15.2] ,[10.3,3,10.3] , [17.6]])

condominio_p1 = assemblyDiagramInit([1,1,8])([[12.3],[10],[4,0.4]*4])
master_condominio = inserts_in_cells(master_condominio , condominio_p1 , [0,2])

apartament = get_master()

toMerge = [11,3,5]
master_condominio = inserts_in_cells(master_condominio , apartament , toMerge)
#VIEW(DRAW_SKEL(master_condominio))
#VIEW(DRAW(master_condominio))


toRemove = [11,13,12,6,5]
master_condominio = removes_cells(master_condominio , toRemove)
#VIEW(DRAW(master_condominio))


toMerge = [8]
terrazzo = assemblyDiagramInit([3,3,3])([[0.4,14.8,0.4] , [0.4,9.9,0.4] , [1.4,0.1,1.5]])
master_condominio = inserts_in_cells(master_condominio , terrazzo , toMerge)

toRemove = [1306]
master_condominio = removes_cells(master_condominio , [1306])
#VIEW(DRAW(master_condominio))

toRemove = [0]
master_condominio = removes_cells(master_condominio , toRemove)

stair_struct = get_stair()
stair_struct = T([1,2])([2,10.5])(stair_struct)
stair_struct = S(3)(1.1)(stair_struct)

#VIEW(STRUCT([stair_struct , DRAW(master_condominio)]))
master_build = STRUCT([stair_struct , DRAW(master_condominio)])
master_build = T([1,3])([10,0.5])(master_build)

terreno = CUBOID([30,30])
terreno = PROD([terreno , Q(0.5)])
terreno = COLOR([0.48,0.62,0.35])(terreno)
#VIEW(terreno)

walk = CUBOID([12,4])
walk = PROD([walk , Q(0.2)])
walk = COLOR([0.57,0.57,0.57])(walk)
walk = T([2,3])([10,0.5])(walk)

####################################
# Costruzione curve
####################################

"""Vaso 2"""
controlPoints = [[0,0,0],[2,0,0.5],[.5,0,1.5],[2,0,2]]
profile = BEZIER(S1)(controlPoints)
obj3 = rotationalSurface2(profile)

vaso1 = COLOR([0.87,0.49,0.37])(T([1,2,3])([5,7,0.5])(obj3))
vaso2 = COLOR([0.87,0.49,0.37])(T([1,2,3])([5,17,0.5])(obj3))


####################################
#  Inserimento alberi
####################################

tree1 = TREE()
tree1 = T([1,2,3])([2,7,0.5])(tree1)
tree2 = T([2,3])([10,0.5])(tree1)
tree3 = T(1)(6)(tree1)
tree4 = T(1)(6)(tree2)

all_structure = STRUCT([master_build , vaso1 , vaso2 , terreno , walk , tree1 , tree2 , tree3 , tree4])
VIEW(all_structure)


