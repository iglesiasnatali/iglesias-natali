"""Proyecto Calculadora - usado como ejemplo para practicar GitFlow.

Contiene las operaciones basicas y una pequena interfaz de linea de comandos.
"""


def sumar(a, b):
    """Devuelve la suma de dos numeros."""
    return a + b


def restar(a, b):
    """Devuelve la resta de dos numeros."""
    return a - b


def dividir(a, b):
    """Devuelve la division de dos numeros.

    Evita el error critico de dividir por cero: antes el programa se
    caia con ZeroDivisionError.
    """
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b


def multiplicar(a, b):
    """Devuelve el producto de dos numeros."""
    return a * b


def main():
    """Punto de entrada por linea de comandos."""
    print("Calculadora basica")
    print(f"2 + 3 = {sumar(2, 3)}")
    print(f"5 - 1 = {restar(5, 1)}")
    print(f"10 / 2 = {dividir(10, 2)}")
    print(f"4 * 6 = {multiplicar(4, 6)}")


if __name__ == "__main__":
    main()
