# Materia: Algoritmos y Estructuras de Datos II
# Alumno/a: Andrés Navarro
# Ejercicio N°: 2
# Fecha de entrega: 23/04/2026

"""
Ejercicio 2:
Programa que solicita dos números al usuario, realiza operaciones básicas
(suma, resta, multiplicación y división) y muestra los resultados.
"""

def solicitar_numero(mensaje):
    """Solicita un número al usuario y valida la entrada."""
    while True:
        try:
            numero = float(input(mensaje))
            return numero
        except ValueError:
            print("Error: Ingrese un número válido.")

def calcular_operaciones(a, b):
    """Realiza operaciones matemáticas básicas."""
    resultados = {
        "suma": a + b,
        "resta": a - b,
        "multiplicacion": a * b,
        "division": None
    }

    if b != 0:
        resultados["division"] = a / b
    else:
        resultados["division"] = "No se puede dividir por cero"

    return resultados

def mostrar_resultados(resultados):
    """Muestra los resultados de las operaciones."""
    print("\nResultados:")
    for operacion, resultado in resultados.items():
        print(f"{operacion.capitalize()}: {resultado}")

def main():
    print("=== Calculadora Básica ===")
    num1 = solicitar_numero("Ingrese el primer número: ")
    num2 = solicitar_numero("Ingrese el segundo número: ")

    resultados = calcular_operaciones(num1, num2)
    mostrar_resultados(resultados)

if __name__ == "__main__":
    main()
