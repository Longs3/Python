def sub(a, b):
	return a-b
def add(a, b):
	return a+b
def div(a, b):
	return a/b
def mul(a, b):
	return a*b
def floor(a):
	return int(a//1)
def ceiling(a):
	if (a%1==0): return int(a)
	return int(a//1+1)
def addCeiling(a, b):
	return add(ceiling(a), ceiling(b))
def subCeiling(a, b):
	return sub(ceiling(a), ceiling(b))
def mulCeiling(a, b):
	return mul(ceiling(a), ceiling(b))
def divCeiling(a, b):
	return div(ceiling(a), ceiling(b))
def addFloor(a, b):
	return add(floor(a), floor(b))
def subFloor(a, b):
	return sub(floor(a), floor(b))
def mulFloor(a, b):
	return mul(floor(a), floor(b))
def divFloor(a, b):
	return div(floor(a), floor(b))
