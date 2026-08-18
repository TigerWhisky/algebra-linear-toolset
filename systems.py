"""
Resolução de Sistemas de Equações Lineares
Métodos: Eliminação de Gauss e Gauss-Jordan
"""

from typing import List, Tuple, Optional
from .matrix import Matrix
from .vector import Vector

def gaussian_elimination(A: Matrix, b: Vector) -> Tuple[Matrix, Vector]:
    """
    Eliminação de Gauss.
    Retorna a matriz triangular superior e o vetor b modificado.
    """
    if not A.is_square():
        raise ValueError("A matriz deve ser quadrada")
    if A.rows != b.dim:
        raise ValueError("Dimensões incompatíveis")

    n = A.rows
    M = A.copy()
    bb = Vector(b.data[:])

    for col in range(n):
        # Pivotagem parcial
        max_row = col
        for i in range(col + 1, n):
            if abs(M.data[i][col]) > abs(M.data[max_row][col]):
                max_row = i
        M.data[col], M.data[max_row] = M.data[max_row], M.data[col]
        bb.data[col], bb.data[max_row] = bb.data[max_row], bb.data[col]

        pivot = M.data[col][col]
        if abs(pivot) < 1e-12:
            raise ValueError("Matriz singular ou quase singular")

        for i in range(col + 1, n):
            factor = M.data[i][col] / pivot
            for j in range(col, n):
                M.data[i][j] -= factor * M.data[col][j]
            bb.data[i] -= factor * bb.data[col]

    return M, bb

def back_substitution(U: Matrix, b: Vector) -> Vector:
    """Substituição regressiva para matriz triangular superior"""
    n = U.rows
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        s = b.data[i]
        for j in range(i + 1, n):
            s -= U.data[i][j] * x[j]
        x[i] = s / U.data[i][i]
    return Vector(x)

def solve_system(A: Matrix, b: Vector) -> Vector:
    """Resolve Ax = b usando Eliminação de Gauss + substituição regressiva"""
    U, bb = gaussian_elimination(A, b)
    return back_substitution(U, bb)

def gauss_jordan(A: Matrix, b: Vector) -> Vector:
    """
    Método de Gauss-Jordan (forma reduzida por linhas).
    Devolve a solução diretamente.
    """
    if not A.is_square():
        raise ValueError("A matriz deve ser quadrada")
    n = A.rows
    # Matriz aumentada
    aug = [A.data[i][:] + [b.data[i]] for i in range(n)]

    for col in range(n):
        # Pivotagem
        max_row = col
        for i in range(col + 1, n):
            if abs(aug[i][col]) > abs(aug[max_row][col]):
                max_row = i
        aug[col], aug[max_row] = aug[max_row], aug[col]

        pivot = aug[col][col]
        if abs(pivot) < 1e-12:
            raise ValueError("Matriz singular")

        # Normalizar linha do pivot
        for j in range(col, n + 1):
            aug[col][j] /= pivot

        # Eliminar outras linhas
        for i in range(n):
            if i == col:
                continue
            factor = aug[i][col]
            for j in range(col, n + 1):
                aug[i][j] -= factor * aug[col][j]

    return Vector([aug[i][n] for i in range(n)])
