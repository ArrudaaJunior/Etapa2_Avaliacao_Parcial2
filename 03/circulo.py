class Circulo:
	def __init__(self, raio, area=0, perimetro=0):
		self.raio = raio
		self.area = area
		self.perimetro = perimetro

	def calcular_area(self):
		pi = 3.141516
		self.area = pi*(self.raio*self.raio)
		return self.area
	
	def calcular_perimetro(self):
		pi = 3.141516
		self.perimetro = 2*pi*self.raio
		return self.perimetro

	def imprimir(self):
		valores = [self.raio, self.area, self.perimetro]
		print(valores)