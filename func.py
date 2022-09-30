class Math:
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
		return Math.add(Math.ceiling(a), Math.ceiling(b))
	def subCeiling(a, b):
		return Math.sub(Math.ceiling(a), Math.ceiling(b))
	def mulCeiling(a, b):
		return Math.mul(Math.ceiling(a), Math.ceiling(b))
	def divCeiling(a, b):
		return Math.div(Math.ceiling(a), Math.ceiling(b))
	def addFloor(a, b):
		return Math.add(Math.floor(a), Math.floor(b))
	def subFloor(a, b):
		return Math.sub(Math.floor(a), Math.floor(b))
	def mulFloor(a, b):
		return Math.mul(Math.floor(a), Math.floor(b))
	def divFloor(a, b):
		return Math.div(Math.floor(a), Math.floor(b))

class Bitwise:
	def lShift(value, unitShift):
		try:
			int(unitShift)
			int(value)
		except ValueError:
			print('invalid value')
			return
		return value << unitShift
	def rShift(value, unitShift):
		try:
			int(unitShift)
			int(value)
		except ValueError:
			print('invalid value')
			return
