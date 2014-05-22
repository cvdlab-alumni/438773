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

   
"""Creazione di un balcone"""
shape = [5,2,3]
dimension = [[2,0.1,7.8,0.1,2] , [1.5,0.1] , [0.15,1.5,0.1]]

master = assemblyDiagramInit(shape)(dimension)
VIEW(DRAW(master))
VIEW(DRAW_SKEL(master))


