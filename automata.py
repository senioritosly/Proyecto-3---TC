#python3
import enum
class Estado():
	def __init__(self, valor):
		self.valor = valor
		self.transiciones = {}

	def agregarTransicion(self, transicion):
		self.transiciones[transicion.read] = transicion

	def movimiento(self, symbol):
		try:
			transicion = self.transiciones[symbol]
			return transicion.sigEstado, transicion.write, transicion.direction
		except KeyError as e:
			return self, None, None

class Transicion():
	class Direccion(enum.Enum):
		DERECHA = 1
		IZQUIERDA  = 2
		NONE = 3

	def __init__(self, read, write, sigEstado, direction):
		self.read = read
		self.write = write
		self.sigEstado = sigEstado
		self.direction = direction