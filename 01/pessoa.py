class Pessoa:
	def __init__(self, nome, endereco, telefone):
		self.nome = nome
		self.endereco = endereco
		self.telefone = telefone

	def imprimir(self):
		valores = [self.nome, self.endereco, self.telefone]
		print(valores)

