import sys
from metodos_numericos.horner import evaluar_horner
from metodos_numericos.muller import metodo_muller
from metodos_numericos.interpolacion import (
    interpolacion_lineal,
    evaluar_lagrange,
    polinomio_lagrange
)
from metodos_numericos.regresion import regresion_lineal

def mostrar_menu():
    """Muestra el menú principal con las opciones disponibles"""
    print("\n" + "="*50)
    print(" MENÚ PRINCIPAL - MÉTODOS NUMÉRICOS ".center(50))
    print("="*50)
    print("1. Evaluación polinomial (Método de Horner)")
    print("2. Determinación de raíces (Método de Müller)")
    print("3. Interpolación lineal")
    print("4. Evaluación polinomial (Método de Lagrange)")
    print("5. Determinación de polinomio de Lagrange")
    print("6. Regresión lineal (Mínimos cuadrados)")
    print("0. Salir")
    print("="*50)

def obtener_polinomio():
    """Solicita al usuario ingresar los coeficientes de un polinomio"""
    print("\nIngrese los coeficientes del polinomio (de mayor a menor grado):")
    coeficientes = []
    while True:
        try:
            n = int(input("Grado del polinomio: "))
            if n < 0:
                raise ValueError
            break
        except ValueError:
            print("Error: Ingrese un número entero no negativo")
    
    for i in range(n, -1, -1):
        while True:
            try:
                coef = float(input(f"Coeficiente para x^{i}: "))
                coeficientes.append(coef)
                break
            except ValueError:
                print("Error: Ingrese un número válido")
    
    return coeficientes

def obtener_puntos():
    """Solicita al usuario ingresar puntos (x,y)"""
    puntos = []
    print("\nIngrese los puntos (x,y). Deje x vacío para terminar.")
    while True:
        x = input("Valor de x: ")
        if not x:
            break
        try:
            x = float(x)
            y = float(input("Valor de y: "))
            puntos.append((x, y))
        except ValueError:
            print("Error: Ingrese números válidos")
    return puntos

def main():
    """Función principal del programa"""
    while True:
        mostrar_menu()
        try:
            opcion = int(input("\nSeleccione una opción: "))
        except ValueError:
            print("Error: Ingrese un número válido")
            continue
        
        if opcion == 0:
            print("\n" + "="*50)
            print("¡Gracias por usar el programa! ")
            print("Hasta luego, puedes cerrar la ventana.")
            print("="*50)
            sys.exit()
        
        elif opcion == 1:  # Horner
            coef = obtener_polinomio()
            x = float(input("Valor de x para evaluar: "))
            resultado = evaluar_horner(coef, x)
            print(f"\nResultado: f({x}) = {resultado}")
        
        elif opcion == 2:  # Müller
            coef = obtener_polinomio()
            print("Ingrese tres puntos iniciales:")
            x0 = float(input("x0: "))
            x1 = float(input("x1: "))
            x2 = float(input("x2: "))
            raiz = metodo_muller(coef, x0, x1, x2)
            print(f"\nRaíz encontrada: {raiz}")
        
        elif opcion == 3:  # Interpolación lineal
            puntos = obtener_puntos()
            if len(puntos) < 2:
                print("Se necesitan al menos 2 puntos")
                continue
            x = float(input("Valor de x para interpolar: "))
            resultado = interpolacion_lineal(puntos, x)
            print(f"\nValor interpolado en x={x}: {resultado}")
        
        elif opcion == 4:  # Evaluación Lagrange
            puntos = obtener_puntos()
            x = float(input("Valor de x para evaluar: "))
            resultado = evaluar_lagrange(puntos, x)
            print(f"\nValor interpolado en x={x}: {resultado}")
        
        elif opcion == 5:  # Polinomio Lagrange
            puntos = obtener_puntos()
            coef = polinomio_lagrange(puntos)
            print("\nCoeficientes del polinomio (de mayor a menor grado):")
            for i, c in enumerate(coef):
                print(f"x^{len(coef)-1-i}: {c}")
        
        elif opcion == 6:  # Regresión lineal
            puntos = obtener_puntos()
            try:
                if len(puntos) < 2:
                    raise ValueError("Se necesitan al menos 2 puntos")
                
                a, b, r2 = regresion_lineal(puntos)
                print(f"\nEcuación de la recta: y = {a:.4f}x + {b:.4f}")
                print(f"Coeficiente de determinación (R²): {r2:.4f}")
                
                # Explicación adicional cuando el intercepto es cercano a cero
                if abs(b) < 1e-10:
                    print("\nNota: El término independiente es aproximadamente cero")
                    print("lo que indica que la recta pasa cerca del origen (0,0).")
                    
            except ValueError as e:
                print(f"\nError en regresión lineal: {e}")
        
        else:
            print("Opción no válida. Intente nuevamente.")

        input("\nPresione Enter para regresar al menú principal...")

if __name__ == "__main__":
    main()