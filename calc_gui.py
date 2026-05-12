
from tkinter import *
from calc_back import sumar, restar, multiplicar, dividir, limpiar

root = Tk()
root.title("Calculadora")
root.resizable(0, 0)

# Dimensiones de la ventana
ancho = 420
alto = 500
root.geometry(f"{ancho}x{alto}")
for col in range(4):
    root.grid_columnconfigure(col, weight=1)

# Pantalla de la calculadora
pantalla = Entry(root, font=("Arial", 14), bd=3, relief=RIDGE, justify=RIGHT)
pantalla.grid(row=0, column=0, columnspan=4, padx=5, pady=10, sticky="we")

# Botones de la calculadora
botones = [
	["7", "8", "9", "/"],
	["4", "5", "6", "*"],
	["1", "2", "3", "-"],
	["0", ".", "=", "+"]
]


# Variables para la operación
valor1 = None
operador = None
nuevo_numero = False


def format_result(resultado):
	if isinstance(resultado, float):
		if resultado.is_integer():
			return str(int(resultado))
		return str(resultado)
	return str(resultado)


def click_boton(valor):
	global nuevo_numero
	if nuevo_numero:
		pantalla.delete(0, END)
		nuevo_numero = False
	pantalla.insert(END, valor)
	pantalla.xview_moveto(1)


def click_operador(op):
	global valor1, operador, nuevo_numero
	valor1 = pantalla.get()
	operador = op
	pantalla.delete(0, END)
	nuevo_numero = False


def click_igual():
	global valor1, operador, nuevo_numero
	valor2 = pantalla.get()
	try:
		if operador == "+":
			resultado = sumar(valor1, valor2)
		elif operador == "-":
			resultado = restar(valor1, valor2)
		elif operador == "*":
			resultado = multiplicar(valor1, valor2)
		elif operador == "/":
			resultado = dividir(valor1, valor2)
		else:
			resultado = valor2
		pantalla.delete(0, END)
		pantalla.insert(0, format_result(resultado))
		pantalla.xview_moveto(1)
		nuevo_numero = True
	except Exception:
		pantalla.delete(0, END)
		pantalla.insert(0, "Error")
		nuevo_numero = True


def click_limpiar():
	pantalla.delete(0, END)
	pantalla.xview_moveto(0)
	global valor1, operador, nuevo_numero
	valor1 = None
	operador = None
	nuevo_numero = False

for i, fila in enumerate(botones):
	for j, texto in enumerate(fila):
		if texto in ["+", "-", "*", "/"]:
			btn = Button(root, text=texto, font=("Arial", 18), width=5, height=2, bd=3,
						 command=lambda t=texto: click_operador(t))
		elif texto == "=":
			btn = Button(root, text=texto, font=("Arial", 18), width=5, height=2, bd=3,
						 command=click_igual)
		else:
			btn = Button(root, text=texto, font=("Arial", 18), width=5, height=2, bd=3,
						 command=lambda t=texto: click_boton(t))
		btn.grid(row=i+1, column=j, padx=5, pady=5)

# Botón de limpiar (C)
btn_clear = Button(root, text="C", font=("Arial", 18), width=26, height=2, bd=3, command=click_limpiar)
btn_clear.grid(row=5, column=0, columnspan=4, padx=5, pady=10)

root.mainloop()
