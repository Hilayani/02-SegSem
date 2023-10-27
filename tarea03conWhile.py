from guizero import App, Box, Text, PushButton, TextBox

# Función para calcular y mostrar el producto
def calcular_producto():
    resultado_text.clear()
    try:
        i = int(input_i.value)
        producto = 1  # Inicializamos el producto en 1
        j = 2
        while j <= 2 * i:
            producto *= 2 * (j - 1) * (2 * j)
            j += 1
        resultado_text.value = f"El producto es: {producto}"
    except ValueError:
        resultado_text.value = "Ingresa un valor válido para i."

# Crear la aplicación
app = App("Cálculo de Producto")

# Crear una caja para organizar los elementos
box = Box(app, layout="grid")

# Etiqueta y campo de entrada para el valor de i
text_i = Text(box, text="Ingresa el valor de i:", grid=[0, 0])
input_i = TextBox(box, grid=[1, 0])

# Botón para calcular
calcular_button = PushButton(box, text="Calcular", command=calcular_producto, grid=[0, 1, 2, 1])

# Campo de texto para mostrar el resultado
resultado_text = Text(box, text="", grid=[0, 2, 2, 1])

# Ejecutar la aplicación
app.display()