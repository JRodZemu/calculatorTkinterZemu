from tkinter import *

root = Tk()
root.title("Calculadora de prueba")
root.overrideredirect(True)
root.resizable(0,0)

root.update_idletasks()

# Método para centrarlo en medio. No me gusta, ya que en doble monitor podría fallar
# width = 500
# height = 500
# width_screen = root.winfo_screenwidth()
# height_screen = root.winfo_screenheight()
# x = (width_screen // 2) - (width // 2)
# y = (height_screen // 2) - (height // 2)
# root.geometry(f"{width}x{height}+{x}+{y}")



root.mainloop()
