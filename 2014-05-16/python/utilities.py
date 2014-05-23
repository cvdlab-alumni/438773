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

"""Funzione che permette di visualizzare la numerazione delle celle dato un master"""

def view_numerating_cells(master):
	hpc = SKEL_1(STRUCT(MKPOLS(master)))
	hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
	VIEW(hpc)

"""Funzione che prende un modello (C,CV), un insieme di indici di celle (indices_remove) e un booleano
	ed elimina tutte le celle con indice contenuto in indices_remove dal modello.
	Se view_final_res = true stampa il risultato finale"""

def removes_cells((V,CV) , indices_remove , view_final_res = False):
	indices_remove.sort(reverse=True)
	model = V,[cell for k,cell in enumerate(CV) if not (k in indices_remove)]
	if(view_final_res): view_numerating_cells(model)
	return model


"""Poiche' la numerazione delle celle una volta inserita una nuova celle di indice x viene 
	fatta da x+1 in poi, basta ordinare in maniera decrescente l'array"""

def inserts_in_cells(master , diagram , cells):
	cells.sort(reverse=True)
	for i,item in enumerate(cells):
		master = diagram2cell(diagram , master , item)
	return master

def general_operation(master , diagram , to_add , to_remove , view_final_res = False):
	master = inserts_in_cells(master , removes_cells(diagram , to_remove) , to_add)
	if(view_final_res): view_numerating_cells(model)
	return master



def rotationalSurface2(profile):
	domain = EMBED(1)(PROD([ Hpc(Grid([10*[1./10]])),  Hpc(Grid([30*[2*PI/30]])) ]))
	mapping = ROTATIONALSURFACE(profile)
	obj = MAP(mapping)(domain)
	return obj

def create_profile(controlPoints):
	b1 = BEZIER(S1)(controlPoints[0])
	b2 = BEZIER(S1)(controlPoints[1])
	profile = BEZIER(S1)([b1,b2])
	return profile
