


"""Set di funzioni per mappare i veritici di V.
	Prima ogni elemento di V viene reso stringa
	Successivamente per ogni elemento di V vengono calcolati i relativi indici creando una mappa
	Ora V e' una mappa dove la chiave e' una stringa e il valore sono gli indici di quella determinata stringa
	che rappresenta il vertice"""
	
def toString(item):
	return str(item)

def toVerts(item):
	return eval(item)

def list2listString(items):
	return map(toString , items)

def scan_verts(V):
	map_obj = {}
	for i,item in enumerate(V):
		map_obj[item] = get_indexs(V,item)
	return map_obj

def get_indexs(V,element):
	indexes = []
	for i,item in enumerate(V):
		if element == item:
			indexes.append(i)
	return indexes


"""Ora creao un set di funzioni con questa logica, 
	Scansiono CV e per gli elemeti che hanno piu' di un indice sostiuisco il secondo, terzo ecc indice
	con il valore del primo nella lista degli indici di quell'elemento"""

def substitute_multiple_index(indexes , CV):
	new_CV = []
	for i,item in enumerate(CV):
		if elementInArray(item , indexes): 
			new_CV.append(filterElement(item , indexes))
		else: 
			new_CV.append(item)
	return new_CV


def elementInArray(items , indexes):
	for i,item in enumerate(items):
		if item in indexes:
			return True
	return False


def filterElement(verts , indexes):
	elements = [a for a in verts if a not in indexes]
	elements.append(indexes[0])
	return elements


def remove_multiple_verts((V,CV)):
	v_str = map(toString , V)
	verts2index = scan_verts(v_str)
	all_indexes = verts2index.values()
	for i,index in enumerate(all_indexes):
		CV = substitute_multiple_index(index , CV)
	v_str  = list(set(verts2index.keys()))
	V = map(toVerts,v_str)
	return (V,CV)



