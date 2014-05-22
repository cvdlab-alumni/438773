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


def view_numerating_cells(master):
	hpc = SKEL_1(STRUCT(MKPOLS(master)))
	hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,0.5)
	VIEW(hpc)


def removes_cells((V,CV) , indices_remove , view_final_res = False):
	model = V,[cell for k,cell in enumerate(CV) if not (k in indices_remove)]
	if(view_final_res): view_numerating_cells(model)
	return model