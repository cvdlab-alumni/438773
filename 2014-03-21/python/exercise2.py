
from pyplasm import *

def disk2D(p):
	u,v = p
	return [v*COS(u), v*SIN(u)]

def create_floor(f):
	floors = []
	f1 = f
	for i in range(1,8):
		f1 = T([1,2])([0.45,2.5])(SCALE([1,2])([0.9,0.9])(f1))
		floors.append(f1)
	return floors


domain2D = PROD([INTERVALS(2*PI)(32), INTERVALS(0.25)(1)])
disk = T([1,2])([0.25,1])(MAP(disk2D)(domain2D))
rect = PROD([QUOTE([0.5]) , QUOTE([1])])

window = COLOR(BROWN)(STRUCT([disk , rect]))
#VIEW(window)

face = PROD([QUOTE([10]) , QUOTE([2])])
floor_face = STRUCT([face , T([1])([5])(window)])
#VIEW(floor_face1)
#north = PROD([QUOTE([10] , QUOTE([2]))])

points = [[10,2] , [10.25 , 2.25] , [10 , 2.5] , [0 , 2] , [0 , 2.50] , [-0.25 , 2.25]]
P = AA(MK)(points)
S = AA(JOIN)(P)
H = JOIN(S)

cover = COLOR(BROWN)(H)
floor_face1 = STRUCT([cover , floor_face])

north = STRUCT([fl for fl in create_floor(floor_face1)])
VIEW(north)