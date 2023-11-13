from automata import *

class Cinta():
	def __init__(self, celdas):
		contador = 0
        
		for i in range(len(celdas)):
			if celdas[i] == '0':
				contador += 1
		self.enesimo_fibonacci = self.calcularEnesimoFibonacci(contador)
		resultado = self.ultimosDosFibonacci(contador)
		n1, n2 = resultado
		tapeCells = '0'*n1 + "c" + '0'*n2 + "B"*100
		self.celdas = tapeCells
		self.position = 0
	
	def calcularEnesimoFibonacci(self, n):
		if n == 0:
			return 0
		elif n == 1:
			return 1
		else:
			a, b = 0, 1
			for _ in range(1, n):
				a, b = b, a + b
			return b
		
	def ultimosDosFibonacci(self,n):
		if n <= 1:
			return (0, 1) if n == 1 else (1, 0)
		else:
			fib_n_minus_1, fib_n_minus_2 = self.ultimosDosFibonacci(n-1)
			fib_n = fib_n_minus_1 + fib_n_minus_2
			return fib_n_minus_2, fib_n

	def finalizo(self):
		return self.position < 0 or self.position >= len(self.celdas)

	def inicio(self):
		if self.finalizo():
			return -1
		return self.celdas[self.position]

	def reset (self):
		self.position = 0

	def posInicio(self):
		return self.position

	def reescribirPosicion(self, symbol):
		pos = self.position
		self.celdas = self.celdas[:pos] + symbol + self.celdas[pos + 1:]
	
	def update(self, toWrite, direction):
		if self.finalizo():
			raise Exception('End of computation.')
		self.reescribirPosicion(toWrite)
		if direction == Transicion.Direccion.DERECHA:
			self.position += 1
		elif direction == Transicion.Direccion.IZQUIERDA:
			self.position -= 1
		elif direction == Transicion.Direccion.NONE:
			pass

class TuringMachine():
	def __init__(self):
		self.estados = {}
		self.estadoActual = None
		self.cinta = None
		self.chequeado = set()
		self.simulando = True
		self.estadoInicial = None

	def agregarEstado(self, state):
		self.estados[state.valor] = state

	def agregarTransicion(self, sourceState, transicion):
		self.estados[sourceState].agregarTransicion(transicion)

	def setEstadoInicial (self, state):
		self.estadoActual = self.estados[state]
		self.estadoInicial = self.estados[state]

	def setCinta (self, tp):
		self.cinta = tp

	def repetir(self):
		self.estadoActual = self.estadoInicial
		self.cinta.reset()
		self.simulando = True
		self.chequeado = {(self.estadoActual.valor, self.cinta.posInicio())}
		computacion = "Estado:" + "(%3s) "%(self.estadoActual.valor)
		computacion += self.cinta.celdas + "\n" + "            "
		computacion += " " * self.cinta.posInicio() + "^\n"
		return computacion

	def getEstado (self, stateValue):
		return self.estados[stateValue]

	def simularMovimiento(self):
		if not self.simulando:
			return "Stop.\n"
		self.estadoActual, toWrite, self.direction = self.estadoActual.movimiento(self.cinta.inicio())
		if toWrite:
			self.cinta.update(toWrite, self.direction)
		if toWrite == None or self.cinta.finalizo():
			self.simulando = False
			return "\nFin\n"
		else:
			computacion = "Estado:" + "(%3s) "%(self.estadoActual.valor)
			computacion += self.cinta.celdas + "\n" + "            "
			computacion += " " * self.cinta.posInicio() + "^\n"
			return computacion

	def simular(self):
		f = open("computacion.txt", "a")
		f.write("Inicio\n\n")
		f.write(self.repetir())
		while self.simulando:
			logEntry = self.simularMovimiento()
			f.write(logEntry);
		f.write("--------------------------------------\n")