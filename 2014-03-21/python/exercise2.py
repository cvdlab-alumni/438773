
def disk2D(p):
	u,v = p
	return [v*COS(u), v*SIN(u)]

def create_floor(f):
	floors = []
	f1 = f
	for i in range(1,8):
		f1 = T([1,3])([0.45,2.5])(SCALE([1,3])([0.9,0.9])(f1))
		floors.append(f1)
	return floors


domain2D = PROD([INTERVALS(2*PI)(32), INTERVALS(0.25)(1)])
disk = T([1,3])([0.25,1])(MAP(disk2D)(domain2D))

verts1 = [[0.65 ,0, 0] , [0.65 , 0 , 1] , [0.15 , 0, 0] , [0.15 , 0 , 1]]
cells1 = [[1,2,3,4]]
pols1 = [[1]]

#rect = PROD([QUOTE([0.5]) , QUOTE([1])])
#rect2 = MAP([S1,S3])(rect)
rect = MKPOL([verts1 , cells1 , pols1])
window = COLOR(BROWN)(STRUCT([rect, disk]))

verts = [[0,0,0] , [0,0,2] , [10,0,2] , [10,0,0]]
cells = [[1,2,3,4]]
pols = [[1]]
face = COLOR(WHITE)(MKPOL([verts,cells,pols]))

floor_face = STRUCT([face , T([1])([5])(window)])
#VIEW(floor_face1)
#north = PROD([QUOTE([10] , QUOTE([2]))])

points = [[10, 0, 2] , [10.25 ,0, 2.25] , [10 , 0, 2.5] , [0 ,0, 2] , [0 , 0,  2.50] , [-0.25 ,0, 2.25]]
P = AA(MK)(points)
S = AA(JOIN)(P)
H = JOIN(S)

cover = COLOR(BROWN)(H)

floor_face1 = STRUCT([cover , floor_face])

north = STRUCT([fl for fl in create_floor(floor_face1)])
east = T(1)(10)(ROTATE([1,2])(-PI/2)(north))
sud = T(2)(-10)(ROTATE([1,2])(PI/2)(north))
ovest = T([1,2])([-10 , -10])(ROTATE([1,2])(PI/2)(T(2)(-10)(sud)))

#Create Top 
verts = [[4,0,0],[4,0,4],[2,0,6]]
top = JOIN(AA(MK)(verts))

north = STRUCT([north , top])
VIEW(north)

faces = STRUCT([north , east , sud , ovest])

faces = T([2,3])([10,-2.5])(faces)

wall0 = PROD([QUOTE([10]) , QUOTE([10])])
internal0 = T([1,2])([0.5,0.5])(PROD([QUOTE([9]) , QUOTE([9])]))
floor0 = STRUCT([wall0 , COLOR(BROWN)(internal0)])

wall1 = T([1,2,3])([0.45,0.45,2])(SCALE([1,2])([0.90,0.90])(wall0))
internal1 = T([1,2,3])([0.45,0.45,2])(SCALE([1,2])([0.90,0.90])(internal0))
floor1 = STRUCT([wall1 , COLOR(RED)(internal1)])

wall2 = T([1,2,3])([0.45,0.45,2])(SCALE([1,2])([0.9,0.9])(wall1))
internal2 = T([1,2,3])([0.45,0.45,2])(SCALE([1,2])([0.90,0.90])(internal1))
floor2 = STRUCT([wall2 , COLOR(YELLOW)(internal2)])

wall3 = T([1,2,3])([0.45,0.45,2])(SCALE([1,2])([0.9,0.9])(wall2))
internal3 = T([1,2,3])([0.45,0.45,2])(SCALE([1,2])([0.90,0.90])(internal2))
floor3 = STRUCT([wall3 , COLOR(GREEN)(internal3)])

wall4 = T([1,2,3])([0.45,0.45,2])(SCALE([1,2])([0.9,0.9])(wall3))
internal4 = T([1,2,3])([0.45,0.45,2])(SCALE([1,2])([0.90,0.90])(internal3))
floor4 = STRUCT([wall4 , COLOR(ORANGE)(internal4)])

wall5 = T([1,2,3])([0.45,0.45,2])(SCALE([1,2])([0.9,0.9])(wall4))
internal5 = T([1,2,3])([0.45,0.45,2])(SCALE([1,2])([0.90,0.90])(internal4))
floor5 = STRUCT([wall5 , COLOR(BLACK)(internal5)])

wall6 = T([1,2,3])([0.45,0.45,2])(SCALE([1,2])([0.9,0.9])(wall5))
internal6 = T([1,2,3])([0.45,0.45,2])(SCALE([1,2])([0.90,0.90])(internal5))
floor6 = STRUCT([wall6 , COLOR(CYAN)(internal6)])

floors = STRUCT([floor0 , floor1 , floor2 , floor3 , floor4 , floor5 , floor6])

#VIEW(STRUCT([floors , faces]))













