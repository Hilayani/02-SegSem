from guizero import App, TextBox, PushButton, Text

# Función para calcular la notación de producto ∏ con la regla (i-1)*i usando un bucle for
def calcular_productoria():
    n = int(input_numero.value)
    resultado_productoria = 1  # Inicializar el resultado en 1
    for i in range(1, n + 1):
        termino = (i - 1) * i
        resultado_productoria *= termino
    resultado_productoria_text.value = f"El resultado de la notacion es: {resultado_productoria}"

# Crear la aplicación
app = App("Notación de Producto ∏")

# Texto al lado del cuadro de texto
Text(app, text="Ingrese i:")

# Crear un cuadro de texto
input_numero = TextBox(app)

# Crear un botón para calcular la notación de producto y la sumatoria
calcular_button = PushButton(app, text="Calcular", command=calcular_productoria)

# Texto para mostrar el resultado de la notación de producto
resultado_productoria_text = Text(app, text="Resultado de la notación de producto: ")

app.display()