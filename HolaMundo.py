def suma_recursiva(a, b):
    if b == 0:
        return a
    else:
        return suma_recursiva(a ^ b, (a & b) << 1)

def resta_recursiva(a, b):
    if b == 0:
        return a
    else:
        return resta_recursiva(a ^ b, (~a & b) << 1)

# Ejemplo de uso
num1 = 10
num2 = 5
print("Suma de", num1, "+", num2, "=", suma_recursiva(num1, num2))
print("Resta de", num1, "-", num2, "=", resta_recursiva(num1, num2))
