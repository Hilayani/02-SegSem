from guizero import App, TextBox, PushButton, Text

# Función para calcular la sumatoria sigma con la regla 2(i-1) + 2i usando un bucle while
def calcular_sumatoria():
    n = int(input_numero.value)
    resultado = 0
    i = 2
    while i <= 2 * n:
        termino = 2 * (i - 1) + 2 * i
        resultado += termino
        i += 1
    resultado_text.value = f"El resulado de la sumatoria es: {resultado}"

# Crear la aplicación
app = App("Sumatoria Sigma")

# Texto al lado del cuadro de texto
Text(app, text="Ingrese i:")

# Crear un cuadro de texto
input_numero = TextBox(app)

# Crear un botón para calcular la sumatoria
calcular_button = PushButton(app, text="Calcular", command=calcular_sumatoria)

# Texto para mostrar el resultado final
resultado_text = Text(app, text="Resultado: ")

app.display()