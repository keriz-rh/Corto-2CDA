def regresion_lineal(puntos):
    """
    Calcula la regresión lineal por mínimos cuadrados con precisión mejorada
    
    Args:
        puntos: Lista de tuplas (x, y) con los datos a analizar
    
    Returns:
        Tuple (pendiente, intercepto, r_cuadrado): Donde:
            pendiente (float): Coeficiente 'a' de y = ax + b
            intercepto (float): Coeficiente 'b' de y = ax + b
            r_cuadrado (float): Coeficiente de determinación
    
    Raises:
        ValueError: Si hay menos de 2 puntos o si no hay variación en x
    """
    # Validación de entrada
    if len(puntos) < 2:
        raise ValueError("Se necesitan al menos 2 puntos para la regresión")
    
    n = len(puntos)
    sum_x = sum_y = sum_xy = sum_x2 = sum_y2 = 0.0
    
    # Cálculo de sumatorias
    for x, y in puntos:
        sum_x += x
        sum_y += y
        sum_xy += x * y
        sum_x2 += x**2
        sum_y2 += y**2
    
    # Cálculo de la pendiente (a)
    denominador = n * sum_x2 - sum_x**2
    if denominador == 0:
        raise ValueError("No se puede calcular: todos los x son iguales")
    
    a = (n * sum_xy - sum_x * sum_y) / denominador
    
    # Cálculo del intercepto (b)
    b = (sum_y - a * sum_x) / n
    
    # Cálculo del coeficiente de determinación R²
    numerador_r = (n * sum_xy - sum_x * sum_y)**2
    denominador_r = (n * sum_x2 - sum_x**2) * (n * sum_y2 - sum_y**2)
    r_cuadrado = numerador_r / denominador_r if denominador_r != 0 else 1.0
    
    # Redondeo para presentación
    a_redondeado = round(a, 10)
    b_redondeado = round(b, 10)
    r_redondeado = round(r_cuadrado, 10)
    
    # Ajuste para evitar -0.0
    if abs(b_redondeado) < 1e-10:
        b_redondeado = 0.0
    
    return a_redondeado, b_redondeado, r_redondeado