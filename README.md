# Calculadora con Python (Tkinter)

Calculadora básica con interfaz gráfica (GUI) utilizando `tkinter` y módulo separado para operaciones matemáticas. Incluye manejo de errores, validación de entrada y formateo de resultados.

## 📌 Características

- Operaciones: suma, resta, multiplicación, división.
- Manejo de errores:
  - Entradas no numéricas → `ValueError`.
  - División entre cero → mensaje específico.
- Pantalla que muestra números y resultados.
- Botón `C` para limpiar y reiniciar operación.
- Conversión automática de enteros (ej. `7.0` se muestra como `7`).
- Interfaz responsive (botones adaptados a la ventana).

## 🗂️ Estructura del proyecto

El código se organiza en dos módulos lógicos (aunque pueden estar en un solo archivo, se recomienda separarlos):

- `calc_back.py`: contiene las funciones aritméticas (`sumar`, `restar`, `multiplicar`, `dividir`, `limpiar`).
- `calc_gui.py`: contiene la interfaz gráfica con `tkinter` y la lógica de eventos.

Si actualmente tienes todo en un solo archivo, simplemente crea los dos archivos y distribuye el código como se muestra más abajo.

## ⚙️ Requisitos

- Python 3.6 o superior.
- Tkinter (incluido por defecto en Windows, macOS y la mayoría de distribuciones Linux).

## 🚀 Instalación y ejecución

1. Clona o descarga el proyecto en tu ordenador.
2. Separa el código en dos archivos (o mantén la estructura que prefieras).
3. Ejecuta la calculadora:
   ```bash
   python calc_gui.py
prueba
