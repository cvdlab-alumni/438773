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


"""Funzione che permette di visualizzare la numerazione delle celle dato un master"""

def view_numerating_cells(master):
	hpc = SKEL_1(STRUCT(MKPOLS(master)))
	hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
	VIEW(hpc)

"""Funzione che prende un modello (C,CV), un insieme di indici di celle (indices_remove) e un booleano
	ed elimina tutte le celle con indice contenuto in indices_remove dal modello.
	Se view_final_res = true stampa il risultato finale"""

def removes_cells((V,CV) , indices_remove , view_final_res = False):
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


"""Funzione che permette di visualizzare le celle
def view_insert_cells(master , toMerge):
	cell = MKPOL([master[0],[[v+1 for v in  master[1][toMerge]]],None])
	VIEW((STRUCT([master , cell])))
"""

DRAW = COMP([STRUCT,MKPOLS])
DRAW_SKEL = COMP([SKEL_1,STRUCT,MKPOLS])

"""Test Funzioni"""
shape = [3,3,3]
dimension = [[1,1,1] , [1,1,1] ,[1,1,1]]

"""Assemblamento diagramma"""
master = assemblyDiagramInit(shape)(dimension)
view_numerating_cells(master)

"""Rimozione di un insieme di celle"""
master = removes_cells(master , [0,2,5] , True)
view_numerating_cells(master)

"""Inserimento di un diagram in piu' celle"""
shape2 = [2,2,2]
dimension2 = [[0.5,0.5] , [0.5,0.5]  ,[0.5,0.5]]

diagram = assemblyDiagramInit(shape2)(dimension2)
master = inserts_in_cells(master , diagram , [1,3])

view_numerating_cells(master)
VIEW(DRAW_SKEL(master))

master = general_operation(master, diagram , [20,32] , [2,4,6]  , False)
VIEW(DRAW_SKEL(master))
VIEW(DRAW(master))














