"""
Cálculo de Valores e Vetores Próprios (valores de eigen)
Método da Potência 
"""

from typing import Tuple
from .matrix import Matrix
from .vector import Vector
import random

def power_method(A: Matrix, max_iter: int = 1000, tol: float = 1e-10) -> Tuple[float, Vector]:
    """
    Método da Potência para encontrar o valor próprio de maior módulo
    e o respetivo vetor próprio.
    """
    if not A.is_square():
        raise ValueError("A matriz deve ser quadrada")

    n = A.rows
    # Vetor inicial aleatório
    x = Vector([random.random() for _ in range(n)])
    x = x.normalize()

    eigenvalue = 0.0

    for _ in range(max_iter):
        y = A * x
        # Novo valor próprio (aproximação de Rayleigh)
        new_eigenvalue = x.dot(y)

        # Normalizar
        norm_y = y.norm()
        if norm_y < 1e-14:
            raise ValueError("Vetor nulo encontrado — método falhou")
        x_new = y / norm_y

        # Verificar convergência
        if abs(new_eigenvalue - eigenvalue) < tol and (x_new - x).norm() < tol:
            return new_eigenvalue, x_new

        x = x_new
        eigenvalue = new_eigenvalue

    return eigenvalue, x
