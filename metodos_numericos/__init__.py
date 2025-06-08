"""
Paquete metodos_numericos - Implementación de métodos numéricos para el examen corto #2

Contiene las siguientes implementaciones:
- Evaluación polinomial por el método de Horner
- Determinación de raíces por el método de Müller
- Interpolación lineal y polinómica (Lagrange)
- Regresión lineal por mínimos cuadrados
"""

# Importaciones para exponer las funciones principales al nivel del paquete
from .horner import evaluar_horner
from .muller import metodo_muller
from .interpolacion import (
    interpolacion_lineal,
    evaluar_lagrange,
    polinomio_lagrange
)
from .regresion import regresion_lineal

# Lista de lo que se importa con 'from metodos_numericos import *'
__all__ = [
    'evaluar_horner',
    'metodo_muller',
    'interpolacion_lineal',
    'evaluar_lagrange',
    'polinomio_lagrange',
    'regresion_lineal'
]

# Metadatos del paquete
__version__ = '1.0.0'
__author__ = 'Kevin Armando Rivera Henríquez (RH16042)'
__course__ = 'Cálculo numérico para desarrollo de aplicaciones - CICLO I/2025'