def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Ejemplo de uso
numero = 5
resultado = factorial(numero)
print("El factorial de", numero, "es:", resultado)
