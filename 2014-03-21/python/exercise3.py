def create_floor(f):
	floors = []
	f1 = f
	for i in range(1,8):
		f1 = T([1,2,3])([0.45,0.45,2.5])(SCALE([1,2,3])([0.9,0.9,0.9])(f1))
		floors.append(f1)
	return floors


f = CUBOID([10,10])
wall = PROD([f , QUOTE([2])])

cover = T([1,2,3])([-0.5 , -0.5 , 2])(PROD([CUBOID([11 , 11]) , QUOTE([0.5])]))
cover = COLOR(GRAY)(cover)

verts1 = [[4.75 ,0, 0] , [4.75 , 0 , 1] , [4.25 , 0, 0] , [4.25 , 0 , 1]]
cells1 = [[1,2,3,4]]
pols1 = [[1]]

rect = MKPOL([verts1 , cells1 , pols1])

window = COLOR(BROWN)(STRUCT([rect]))
#window = PROD([window , QUOTE([10])])

floor = STRUCT([cover , wall, window])
#floor = DIFFERENCE([floor , window])

floors =  STRUCT([fls for fls in create_floor(floor)])

VIEW(floors)

base = CUBOID([4.6 , 4.6])
pt = MK([2.3 , 2.3 , 1.5])
top = AA(JOIN)([base , pt])



