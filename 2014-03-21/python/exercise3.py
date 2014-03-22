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
cover = COLOR([0.643 , 0.5174 , 0.376])(cover)

verts1 = [[4.75 ,0, 0] , [4.75 , 0 , 1] , [4.25 , 0, 0] , [4.25 , 0 , 1]]
cells1 = [[1,2,3,4]]
pols1 = [[1]]

rect = MKPOL([verts1 , cells1 , pols1])

window = COLOR(BROWN)(STRUCT([rect]))
window2 = COLOR(BROWN)(ROTATE([1,2])(PI/2)(window))
#window3 = ROTATE([1,2])(PI)(window2)

#window = PROD([window , QUOTE([10])])

floor = COLOR([0.9098, 0.5921, 0.341])(STRUCT([cover , wall, window , window2]))
#floor = DIFFERENCE([floor , window])

floors = STRUCT([fls for fls in create_floor(floor)])

VIEW(floors)








