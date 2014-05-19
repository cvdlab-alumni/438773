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


DRAW = COMP([STRUCT,MKPOLS])
DRAW_SKEL = COMP([SKEL_1,STRUCT,MKPOLS])

shape = [1,3,8]
dimension = [[3] , [0.3,9.6,0.3] , [4,0.4]*4]

master = assemblyDiagramInit(shape)(dimension)
VIEW(DRAW(master))
VIEW(DRAW_SKEL(master))







