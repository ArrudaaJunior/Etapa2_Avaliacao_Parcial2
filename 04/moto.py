class Moto:
	def __init__(self, marca, modelo, cor, marcha,ligada):
		self.marca = marca
		self.modelo = modelo
		self.cor = cor
		self.marcha = marcha
		self.ligada = ligada
	
	def marcha_acima(self):
		maior_marcha = 3
		if(self.marcha > maior_marcha):
			print('Erro, macha maior que a possivel')
		else:	
			self.marcha = self.marcha + 1
			return self.marcha

	def marcha_abaixo(self):
		menor_marcha = 0
		if(self.marcha < menor_marcha):
			print('Erro, macha menor que a possivel')
		else:	
			self.marcha = self.marcha - 1
			return self.marcha

	def ligar(self):
		if(self.ligada == 8):
			self.ligada = 'Moto Ligada'
			return True
		else:
			self.ligada = 'Moto Desligada'
			return False		

	def imprimir(self):
		valores = [self.marca, self.modelo, self.cor, self.ligada, self.marcha]
		print(valores)