import numpy as np
from numpy.polynomial.polynomial import Polynomial

def interpolacion_lineal(puntos, x):
    """
    Realiza interpolación lineal entre dos puntos con validación mejorada
    
    Args:
        puntos: Lista de tuplas (x,y)
        x: Valor a interpolar
    
    Returns:
        Valor interpolado y
    
    Raises:
        ValueError: Si no hay suficientes puntos
    """
    if len(puntos) < 2:
        raise ValueError("Se necesitan al menos 2 puntos para interpolación lineal")
    
    # Ordenar puntos por x y eliminar duplicados
    puntos = sorted({p[0]: p for p in puntos}.values(), key=lambda p: p[0])
    
    # Encontrar intervalo
    for i in range(len(puntos)-1):
        x1, y1 = puntos[i]
        x2, y2 = puntos[i+1]
        if x1 <= x <= x2:
            return y1 + (y2 - y1) * (x - x1) / (x2 - x1)
    
    # Extrapolación con aviso
    print("⚠️ Advertencia: Extrapolando más allá del rango de datos")
    if x < puntos[0][0]:
        x1, y1 = puntos[0]
        x2, y2 = puntos[1]
    else:
        x1, y1 = puntos[-2]
        x2, y2 = puntos[-1]
    
    return y1 + (y2 - y1) * (x - x1) / (x2 - x1)

def evaluar_lagrange(puntos, x, verbose=False):
    """
    Evalúa el polinomio de Lagrange en un punto x con opción de depuración
    
    Args:
        puntos: Lista de tuplas (x,y)
        x: Valor a evaluar
        verbose: Si True, muestra pasos intermedios
    
    Returns:
        Valor del polinomio en x
    
    Raises:
        ValueError: Si hay valores x duplicados
    """
    x_vals = [p[0] for p in puntos]
    if len(x_vals) != len(set(x_vals)):
        raise ValueError("No puede haber valores x duplicados en la interpolación")
    
    n = len(puntos)
    resultado = 0.0
    
    for i in range(n):
        xi, yi = puntos[i]
        term = yi
        if verbose:
            print(f"\nTérmino base {i}: y{i} = {yi}")
            factors = []
        
        for j in range(n):
            if j != i:
                xj = puntos[j][0]
                factor = (x - xj) / (xi - xj)
                term *= factor
                if verbose:
                    factors.append(f"(x-{xj})/({xi}-{xj}) = {factor:.4f}")
        
        if verbose:
            print(" * ".join([f"{yi}"] + factors) + f" = {term:.4f}")
        
        resultado += term
    
    if verbose:
        print(f"\nResultado final: {resultado:.6f}")
    
    return resultado

def polinomio_lagrange(puntos, tol=1e-10):
    """
    Construye el polinomio de Lagrange como coeficientes con mejor manejo numérico
    
    Args:
        puntos: Lista de tuplas (x,y)
        tol: Tolerancia para considerar cero un coeficiente
    
    Returns:
        Coeficientes del polinomio [a_n, ..., a_0]
    
    Raises:
        ValueError: Si hay valores x duplicados
    """
    x_vals = [p[0] for p in puntos]
    if len(x_vals) != len(set(x_vals)):
        raise ValueError("No puede haber valores x duplicados en la interpolación")
    
    n = len(puntos)
    polinomio = np.zeros(n)
    
    for i in range(n):
        xi, yi = puntos[i]
        term = np.array([yi])
        for j in range(n):
            if j != i:
                xj = puntos[j][0]
                denominador = xi - xj
                factor = np.array([1.0, -xj]) / denominador
                term = np.convolve(term, factor)
        polinomio = np.polyadd(polinomio, term)
    
    # Limpieza de coeficientes pequeños
    polinomio = [coef if abs(coef) > tol else 0 for coef in np.round(polinomio, 10)]
    
    # Convertir a Polynomial para mejor representación
    return Polynomial(polinomio[::-1]).coef.tolist()

def graficar_interpolacion(puntos, metodo='lagrange', rango=None):
    """
    Grafica los puntos y la interpolación
    
    Args:
        puntos: Lista de tuplas (x,y)
        metodo: 'lineal' o 'lagrange'
        rango: Tupla (xmin, xmax) para el gráfico
    """
    import matplotlib.pyplot as plt
    
    if not puntos:
        raise ValueError("No hay puntos para graficar")
    
    x_vals = [p[0] for p in puntos]
    y_vals = [p[1] for p in puntos]
    
    if rango is None:
        x_min, x_max = min(x_vals), max(x_vals)
        margen = (x_max - x_min) * 0.2
        x_min -= margen
        x_max += margen
    else:
        x_min, x_max = rango
    
    plt.figure(figsize=(10, 6))
    plt.scatter(x_vals, y_vals, color='red', label='Puntos dados', zorder=5)
    
    if metodo == 'lineal' and len(puntos) >= 2:
        x_plot = np.linspace(x_min, x_max, 500)
        y_plot = [interpolacion_lineal(puntos, x) for x in x_plot]
        plt.plot(x_plot, y_plot, label='Interpolación lineal', linestyle='--')
    elif metodo == 'lagrange' and len(puntos) >= 2:
        coef = polinomio_lagrange(puntos)
        p = np.poly1d(coef[::-1])
        x_plot = np.linspace(x_min, x_max, 500)
        y_plot = p(x_plot)
        plt.plot(x_plot, y_plot, label='Polinomio de Lagrange')
    
    plt.title('Interpolación de puntos')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.show()