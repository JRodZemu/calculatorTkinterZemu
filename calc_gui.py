from tkinter import *

root = Tk()
root.title("Calculadora")
root.resizable(0, 0)

# Dimensiones de la ventana
ancho = 320
alto = 450
root.geometry(f"{ancho}x{alto}")

# Pantalla de la calculadora
pantalla = Entry(root, font=("Arial", 24), bd=10, relief=RIDGE, justify=RIGHT)
pantalla.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="we")

# Botones de la calculadora
botones = [
	["7", "8", "9", "/"],
	["4", "5", "6", "*"],
	["1", "2", "3", "-"],
	["0", ".", "=", "+"]
]

for i, fila in enumerate(botones):
	for j, texto in enumerate(fila):
		btn = Button(root, text=texto, font=("Arial", 18), width=5, height=2, bd=3)
		btn.grid(row=i+1, column=j, padx=5, pady=5)

# Botón de limpiar (C)
btn_clear = Button(root, text="C", font=("Arial", 18), width=22, height=2, bd=3)
btn_clear.grid(row=5, column=0, columnspan=4, padx=5, pady=10)

root.mainloop()
