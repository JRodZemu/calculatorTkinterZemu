# Backend para calculadora

def sumar(a, b):
	try:
		a = float(a)
		b = float(b)
		return a + b
	except (ValueError, TypeError):
		raise ValueError("Entradas inválidas para suma")

def restar(a, b):
	try:
		a = float(a)
		b = float(b)
		return a - b
	except (ValueError, TypeError):
		raise ValueError("Entradas inválidas para resta")

def multiplicar(a, b):
	try:
		a = float(a)
		b = float(b)
		return a * b
	except (ValueError, TypeError):
		raise ValueError("Entradas inválidas para multiplicación")

def dividir(a, b):
	try:
		a = float(a)
		b = float(b)
		if b == 0:
			raise ValueError("No se puede dividir por cero")
		return a / b
	except (ValueError, TypeError):
		raise ValueError("Entradas inválidas para división")

def limpiar():
	return ""
