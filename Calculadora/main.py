"""
Calculadora - Programa principal
Importa el método sumar desde gams_suma y el método restar desde gams_resta
"""

from op_suma import sumar
from op_resta import restar


def mostrar_menu():
    """Muestra el menú de opciones"""
    print("\n=== CALCULADORA ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Salir")


def main():
    """Función principal de la calculadora"""
    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción (1-3): ")
        
        if opcion == "3":
            print("¡Hasta luego!")
            break
        
        if opcion in ["1", "2"]:
            try:
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))
                
                if opcion == "1":
                    resultado = sumar(num1, num2)
                    print(f"\nResultado: {num1} + {num2} = {resultado}")
                else:
                    resultado = restar(num1, num2)
                    print(f"\nResultado: {num1} - {num2} = {resultado}")
                    
            except ValueError:
                print("\nError: Debes ingresar números válidos")
        else:
            print("\nOpción inválida. Por favor selecciona 1, 2 o 3")


if __name__ == "__main__":
    main()
