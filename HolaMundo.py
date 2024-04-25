def calcular_imc(peso, altura):
    # Fórmula del IMC: peso / (altura^2)
    imc = peso / (altura ** 2)
    return imc

def interpretar_imc(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif imc >= 18.5 and imc < 25:
        return "Peso normal"
    elif imc >= 25 and imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"

# Ejemplo de uso
peso = float(input("Ingresa tu peso en kilogramos: "))
altura = float(input("Ingresa tu altura en metros: "))

imc = calcular_imc(peso, altura)
print(f"Tu IMC es: {imc:.2f}")
print("Interpretación del IMC:", interpretar_imc(imc))

