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
def ceilingDiv(a,b):
	return ceiling(div(a,b))
def ceilingSub(a,b):
	return ceiling(sub(a,b))
def ceilingAdd(a,b):
	return ceiling(add(a,b))
def ceilingMul(a,b):
	return ceiling(mul(a,b))
