def evaluar_horner(coeficientes, x):
    """
    Evalúa un polinomio usando el método de Horner
    
    Args:
        coeficientes: Lista de coeficientes [a_n, a_n-1, ..., a_0]
        x: Valor en el que evaluar el polinomio
    
    Returns:
        Valor del polinomio evaluado en x
    """
    resultado = 0
    for coef in coeficientes:
        resultado = resultado * x + coef
    return resultado