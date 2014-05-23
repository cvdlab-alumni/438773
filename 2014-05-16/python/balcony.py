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


def get_balcony_x():
	return master_x;
	

def get_balcony_y():
	return master_y;

"""Creazione di un balcone"""
shape = [1,3,2]
dimension = [[1.7] ,[1,10,1], [1.75,1.25]]
master = assemblyDiagramInit(shape)(dimension)

shape2 = [3,3,3]
dimension2 = [[0.1,1.5,0.1] ,[0.1,9.8,0.1], [0.15,1.5,0.1]]
balcone = assemblyDiagramInit(shape2)(dimension2)

master = inserts_in_cells(master , balcone , [2])

toRemove_y = [2,19,18,10,9]
toRemove_x = [2,19,18,28,27]
master_x = removes_cells(master , toRemove_x)
master_y = removes_cells(master , toRemove_y)

#VIEW(DRAW(master_y))
#VIEW(DRAW(master_x))


