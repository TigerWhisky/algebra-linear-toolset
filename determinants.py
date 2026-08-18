"""
Cálculo das Determinantes e Matriz Inversa
"""

from .matrix import Matrix
from .systems import solve_system
from .vector import Vector

def determinant(A: Matrix) -> float:
    """
    Calcula o determinante usando eliminação de Gauss
    (melhor que o Laplace em matrizes grandes).
    """
    if not A.is_square():
        raise ValueError("A matriz deve ser quadrada")

    n = A.rows
    M = A.copy()
    det = 1.0
    sign = 1

    for col in range(n):
        # Pivotagem parcial
        max_row = col
        for i in range(col + 1, n):
            if abs(M.data[i][col]) > abs(M.data[max_row][col]):
                max_row = i

        if max_row != col:
            M.data[col], M.data[max_row] = M.data[max_row], M.data[col]
            sign *= -1

        pivot = M.data[col][col]
        if abs(pivot) < 1e-12:
            return 0.0

        det *= pivot

        for i in range(col + 1, n):
            factor = M.data[i][col] / pivot
            for j in range(col, n):
                M.data[i][j] -= factor * M.data[col][j]

    return sign * det

def inverse(A: Matrix) -> Matrix:
    """
    Calcula a matriz inversa resolvendo A * X = I
    coluna a coluna.
    """
    if not A.is_square():
        raise ValueError("A matriz deve ser quadrada")
    if abs(determinant(A)) < 1e-12:
        raise ValueError("Matriz singular — não tem inversa")

    n = A.rows
    I = Matrix.identity(n)
    inv_cols = []

    for j in range(n):
        e_j = Vector([I.data[i][j] for i in range(n)])
        col = solve_system(A, e_j)
        inv_cols.append(col.data)

    # Transpor as colunas para obter a matriz inversa
    inv_data = [[inv_cols[j][i] for j in range(n)] for i in range(n)]
    return Matrix(inv_data)
