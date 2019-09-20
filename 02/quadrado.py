class Quadrado:
	def __init__(self, lado, area=0, perimetro=0):
		self.lado = lado
		self.area = area
		self.perimetro = perimetro

	def calcular_perimetro(self):
		self.perimetro = 4 * self.lado
		return self.perimetro


	def calcular_area(self):
		self.area = self.lado * self.lado
		return self.area

	def imprimir(self):
		valores = [self.lado, self.area, self.perimetro]
		print(valores)
