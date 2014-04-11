import sys

from simplexn import *
from larcc import *
from lar2psm import *
from largrid import *
from morph import *
from mapper import *

from pyplasm import *
from larcc import * 

######################################################
# Funzione che crea una lista di hpc, dove ogni hpc 
# corrisponde ad un piano della struttura.
# ogni piano della struttura viene scalato automaticamente
#####################################################

def create_floor(f):
	floors = []
	f1 = f
	floors.append(f1)
	for i in range(1,7):
		f1 = T([1,2,3])([0.45,0.45,3])(SCALE([1,2,3])([0.9,0.9,0.9])(f1))
		floors.append(f1)
	return floors


w1 = CUBOID([10,10])
w1 = PROD([w1, Q(3)])
w2 = CUBOID([9,9])
w2 = T([1,2,3])([0.5,0.5,1])(COLOR(RED)(PROD([w2, Q(2)])))

walls = DIFFERENCE([w1 , w2])

floors = COLOR([0.9098, 0.5921, 0.341])(STRUCT(create_floor(walls)))

VIEW(floors)





