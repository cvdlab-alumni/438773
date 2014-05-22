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


def get_windows():
	return master_w1;

"""Create double Window"""
shape = [6,3,3]
dimension = [[0.1,0.4,0.1,0.1,0.4,0.1] , [0.05,0.2,0.05] , [0.1,1.35,0.1]]
master_w1 = assemblyDiagramInit(shape)(dimension)

toRemove = [10,16,43,37]
master_w1 = removes_cells(master_w1 , toRemove)

#VIEW(DRAW(master_w1))


"""Create single windows"""


shape = [3,3,3]
dimension = [[0.1,0.4,0.1] , [0.05,0.2,0.05] , [0.1,1.35,0.1]]
master_w2 = assemblyDiagramInit(shape)(dimension)

toRemove = [10,16]
master_w2 = removes_cells(master_w2 , toRemove)

#VIEW(DRAW(master_w2))





