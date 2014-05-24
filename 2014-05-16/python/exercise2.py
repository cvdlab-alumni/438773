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


#####################
# Inserimento piani
#####################

master_condominio = assemblyDiagramInit([1,3,1])([[15.2] ,[10.3,3,10.3] , [17.6]])
VIEW(DRAW_SKEL(master_condominio))

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
#view_numerating_cells(master_condominio)


toMerge = [8]
terrazzo = assemblyDiagramInit([3,3,3])([[0.4,14.8,0.4] , [0.4,9.9,0.4] , [1.4,0.1,1.5]])
master_condominio = inserts_in_cells(master_condominio , terrazzo , toMerge)
view_numerating_cells(master_condominio)

toRemove = [1306]
master_condominio = removes_cells(master_condominio , [1306])
VIEW(DRAW(master_condominio))

















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


