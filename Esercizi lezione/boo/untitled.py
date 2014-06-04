'''
from pyplasm import *

DRAW = COMP([VIEW , STRUCT])


tensor_1 = T([1,2])([-.1,-.9])(CUBOID([.2,1]));

#VIEW(link);

rotate_tensor = R([1,2])(PI/6);

#DRAW([rotate_tensor , link]);

tensor_2 = T(2)([-.8])

DRAW([link , tensor_2 , rotate_tensor , link , tensor_2])

def arm(a1 , a2 ,a3):
'''

from pyplasm import *

link = T([1,2])([-.1,-.9])(CUBOID([.2,1]))

def arm(a1,a2,a3): #3 angoli
	return STRUCT([R([1,2])(a1), link, T(2)(-.8), R([1,2])(a2), link, T(2)(-.8), R([1,2])(a3), link])

#ogni trasformazione si applica a tutto quello che segue
#VIEW(STRUCT([link, T(2)(-.8), R([1,2])(PI/4), link, T(2)(-.8), R([1,2])(PI/6), link]))
VIEW(arm(PI/2,PI/6,-PI/4))


