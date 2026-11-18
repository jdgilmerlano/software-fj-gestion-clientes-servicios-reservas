# Prueba de manejo de excepciones - Compañero 4

def probar_try_except():
    try:
        numero = int("abc")
        print(f"El número es: {numero}")

    except ValueError as error:
        print(f"Se produjo un error: {error}")


probar_try_except()
