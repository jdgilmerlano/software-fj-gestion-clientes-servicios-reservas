# Prueba de manejo de excepciones - Compañero 4

from src.excepciones.excepciones_personalizadas import DatoInvalidoError

def probar_try_except():
    try:
        numero = int("abc")
        print(f"El número es: {numero}")

    except ValueError as error:
        print(f"Se produjo un error: {error}")


probar_try_except()

def probar_try_except_else():
    try:
        numero = int("10")

    except ValueError as error:
        print(f"No se pudo convertir el valor: {error}")

    else:
        print(f"La conversión fue exitosa. El número es: {numero}")


probar_try_except_else()

def probar_try_except_finally():
    try:
        numero = int("abc")
        print(f"El número es: {numero}")

    except ValueError as error:
        print(f"Se produjo un error: {error}")

    finally:
        print("La operación ha finalizado.")


probar_try_except_finally()

def probar_encadenamiento():
    try:
        valor = int("abc")
    except ValueError as error:
        raise DatoInvalidoError(
            "El dato recibido no es válido."
        ) from error

probar_encadenamiento()


probar_encadenamiento()
