from guizero import App, TextBox, PushButton, Text

# Función para calcular la sumatoria
def calcular_sumatoria():
    valor_i = int(input_i.value)
    resultado = 0
    i = 1

    while i <= valor_i:
        resultado += (i - 1) ** 3 + i ** 3
        i += 1

    resultado_text.value = f"Resultado: {resultado}"

# Crear una aplicación GUI
app = App("Calculadora de Sumatoria")

# Etiqueta para ingresar el valor de i
i_text = Text(app, "Valor de i:")

# Campo de entrada para el valor de i
input_i = TextBox(app, width=5)

# Botón para calcular la sumatoria
calcular_button = PushButton(app, text="Calcular", command=calcular_sumatoria)

# Etiqueta para mostrar el resultado
resultado_text = Text(app, "")

app.display()