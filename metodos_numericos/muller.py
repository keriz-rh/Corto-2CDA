import cmath
from .horner import evaluar_horner  # Esta es la línea clave que faltaba

def metodo_muller(coeficientes, x0, x1, x2, tol=1e-6, max_iter=100):
    """
    Encuentra una raíz de un polinomio usando el método de Müller
    
    Args:
        coeficientes: Coeficientes del polinomio [a_n, ..., a_0]
        x0, x1, x2: Valores iniciales
        tol: Tolerancia para convergencia
        max_iter: Máximo número de iteraciones
    
    Returns:
        Raíz aproximada del polinomio
    """
    def f(x):
        return evaluar_horner(coeficientes, x)
    
    for _ in range(max_iter):
        fx0, fx1, fx2 = f(x0), f(x1), f(x2)
        
        h1, h2 = x1 - x0, x2 - x1
        delta1, delta2 = (fx1 - fx0)/h1, (fx2 - fx1)/h2
        
        a = (delta2 - delta1) / (h2 + h1)
        b = delta2 + h2 * a
        c = fx2
        
        D = cmath.sqrt(b**2 - 4*a*c)
        q = b + D if abs(b - D) < abs(b + D) else b - D
        
        r = -2 * c / q
        x3 = x2 + r
        
        print(f"Iteración {_+1}: x = {x3}")  # Para depuración
        
        if abs(r) < tol:
            return x3
        
        x0, x1, x2 = x1, x2, x3
    
    raise ValueError("El método no convergió en el número máximo de iteraciones")