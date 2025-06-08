
# Proyecto de Métodos Numéricos - RH16042
## Autor
```
Kevin Armando Rivera Henríquez - RH16042  
Universidad de El Salvador - Ciclo I/2025  
Cálculo Numérico para Desarrollo de Aplicaciones
```
## Descripción
Este proyecto implementa diversos métodos numéricos para:
- Evaluación polinomial (Horner)
- Cálculo de raíces (Método de Müller)
- Interpolación (lineal y Lagrange)
- Regresión lineal por mínimos cuadrados

## Estructura del Proyecto
```m
RH16042/
│
├── main.py                 # Programa principal con menú interactivo
├── metodos_numericos/
│   ├── __init__.py         # Inicialización del paquete
│   ├── horner.py           # Evaluación polinomial
│   ├── muller.py           # Método de Müller para raíces
│   ├── interpolacion.py    # Interpolación lineal y Lagrange
│   └── regresion.py        # Regresión lineal
├── requirements.txt        # Dependencias
└── README.md               # Este archivo
```

## Requisitos
- Python 3.6+
- Bibliotecas:
  ```bash
  pip install numpy matplotlib
  ```

## Instrucciones de Uso
1. Clonar el repositorio
2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecutar el programa:
   ```bash
   python main.py
   ```

## Funcionalidades del Menú

### 1. Evaluación Polinomial (Horner)
Evalúa polinomios usando el método de Horner. Ejemplo:
```
Grado: 2
Coeficientes: 1, -3, 2 (para x² - 3x + 2)
x = 2 → Resultado: 0
```

### 2. Método de Müller
Calcula raíces de polinomios. Ejemplo:
```
Polinomio: x³ - 2x² - 5x + 6
Puntos iniciales: 0, 1, 2
Raíz encontrada: ≈2.0
```

### 3. Interpolación Lineal
Interpola entre puntos. Ejemplo:
```
Puntos: (1,1), (3,9)
x = 2 → y = 5
```

### 4. Evaluación con Lagrange
Evalúa el polinomio de Lagrange en un punto. Ejemplo:
```
Puntos: (1,1), (2,4), (3,9)
x = 2.5 → y = 6.25
```

### 5. Polinomio de Lagrange
Muestra los coeficientes del polinomio. Ejemplo:
```
Puntos: (0,2), (1,1), (2,4)
Resultado: 1.5x² - 2.5x + 2
```

### 6. Regresión Lineal
Calcula la recta de mejor ajuste. Ejemplo:
```
Puntos: (1,1), (2,3), (3,3), (4,5)
Resultado: y = 1.2x + 0.0, R²=0.9231
```

## Documentación Técnica
- **Precisión**: Todos los cálculos usan precisión de 10 decimales
- **Validaciones**: Incluye manejo de errores para entradas inválidas
- **Visualización**: Opción para graficar resultados (requiere matplotlib)

## Autor
Kevin Armando Rivera Henríquez - RH16042  
Universidad de El Salvador - Ciclo I/2025  
Cálculo Numérico para Desarrollo de Aplicaciones
```
```
# Ejemplos de Interacción con el Menú

## Ejemplo 1: Evaluación Polinomial (Opción 1)
```
Seleccione una opción: 1

Ingrese los coeficientes del polinomio (de mayor a menor grado):
Grado del polinomio: 3
Coeficiente para x^3: 2
Coeficiente para x^2: -4
Coeficiente para x^1: 3
Coeficiente para x^0: -5
Valor de x para evaluar: 2

Resultado: f(2) = 5.0
```

## Ejemplo 2: Método de Müller (Opción 2)
```
Seleccione una opción: 2

Ingrese los coeficientes del polinomio (de mayor a menor grado):
Grado del polinomio: 3
Coeficiente para x^3: 1
Coeficiente para x^2: -0.5
Coeficiente para x^1: 4
Coeficiente para x^0: -3
Ingrese tres puntos iniciales:
x0: 0
x1: 1
x2: 2

Iteración 1: x = (0.6666666666666666+0j)
Iteración 2: x = (0.7236842105263158+0j)
Iteración 3: x = (0.721124885216056+0j)

Raíz encontrada: (0.721124885216056+0j)
```

## Ejemplo 3: Interpolación Lineal (Opción 3)
```
Seleccione una opción: 3

Ingrese los puntos (x,y). Deje x vacío para terminar.
Valor de x: 1
Valor de y: 2
Valor de x: 3
Valor de y: 5
Valor de x: 
Valor de x para interpolar: 2

Valor interpolado en x=2: 3.5
```

## Ejemplo 4: Evaluación con Lagrange (Opción 4)
```
Seleccione una opción: 4

Ingrese los puntos (x,y). Deje x vacío para terminar.
Valor de x: 1
Valor de y: 1
Valor de x: 2
Valor de y: 4
Valor de x: 3
Valor de y: 9
Valor de x: 
Valor de x para evaluar: 2.5

Valor interpolado en x=2.5: 6.25
```

## Ejemplo 5: Polinomio de Lagrange (Opción 5)
```
Seleccione una opción: 5

Ingrese los puntos (x,y). Deje x vacío para terminar.
Valor de x: 0
Valor de y: 2
Valor de x: 1
Valor de y: 1
Valor de x: 2
Valor de y: 4
Valor de x: 

Coeficientes del polinomio (de mayor a menor grado):
x^2: 1.5
x^1: -2.5
x^0: 2.0
```

## Ejemplo 6: Regresión Lineal (Opción 6)
```
Seleccione una opción: 6

Ingrese los puntos (x,y). Deje x vacío para terminar.
Valor de x: 1
Valor de y: 1
Valor de x: 2
Valor de y: 3
Valor de x: 3
Valor de y: 3
Valor de x: 4
Valor de y: 5
Valor de x: 

Ecuación de la recta: y = 1.2000x + 0.0000
Coeficiente de determinación (R²): 0.9231

Nota: El término independiente es aproximadamente cero
lo que indica que la recta pasa cerca del origen (0,0).
```

## Ejemplo de Salida (Opción 0)
```
Seleccione una opción: 0

¡Gracias por usar el programa! Hasta luego, puedes cerrar la ventana.
```
