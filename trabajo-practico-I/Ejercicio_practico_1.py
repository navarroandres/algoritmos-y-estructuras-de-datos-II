Materia: Algoritmos y Estructuras de Datos II
# Alumno/a: Andrés Navarro
# Ejercicio N°: 1
# Fecha de entrega: 23/04/2026

"""
Ejercicio 1:
Programa que solicita el nombre del usuario y muestra un saludo personalizado.
"""

def solicitar_nombre():
    """Solicita al usuario que ingrese su nombre."""
    nombre = input("Ingrese su nombre: ")
    return nombre

def mostrar_saludo(nombre):
    """Muestra un saludo personalizado."""
    print(f"Hola {nombre}, bienvenido al TP 1 de Algoritmos y Estructuras de Datos II")

def main():
    nombre = solicitar_nombre()
    mostrar_saludo(nombre)

if __name__ == "__main__":
    main()
