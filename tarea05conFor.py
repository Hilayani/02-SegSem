from guizero import App, TextBox, PushButton, Text

def calcular_producto():
    num1 = input_num1.value
    num2 = input_num2.value
    
    if num1.isdigit() and num2.isdigit():
        num1 = int(num1)
        num2 = int(num2)
        
        if num1 > 0 and num2 > 0:
            resultado = 0
            for i in range(num2):
                resultado += num1
            label_result.value = f"El producto es {resultado}"
        else:
            label_result.value = "Por favor, ingrese números positivos."
    else:
        label_result.value = "Por favor, ingrese números enteros positivos."

app = App("Calculadora de Producto", width=300, height=150)
Text(app, "Ingrese dos números enteros positivos:")
input_num1 = TextBox(app)
input_num2 = TextBox(app)
calculate_button = PushButton(app, text="Calcular Producto", command=calcular_producto)
label_result = Text(app, "")

app.display()