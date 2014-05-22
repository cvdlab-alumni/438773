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


"""Create door"""
shape = [3,3,2]
dimension = [[0.1,0.72,0.1] , [0.05,0.2,0.05] , [2.1,0.1]]

master = assemblyDiagramInit(shape)(dimension)
master = removes_cells(master , [6,10])

doorsChain = []

VIEW(DRAW(master))



