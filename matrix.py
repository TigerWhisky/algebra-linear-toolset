"""
Implementação de Matrizes em Python
"""

from typing import List, Union
from .vector import Vector

class Matrix:
    def __init__(self, data: List[List[float]]):
        if not data or not data[0]:
            raise ValueError("A Matriz não pode estar vazia")
        self.rows = len(data)
        self.cols = len(data[0])
        for row in data:
            if len(row) != self.cols:
                raise ValueError("As linhas tem de ter o mesmo comprimento")
        self.data = [[float(x) for x in row] for row in data]

    def __repr__(self):
        return f"Matrix({self.data})"

    def __str__(self):
        rows_str = []
        for row in self.data:
            rows_str.append("[" + ", ".join(f"{x:8.4f}" for x in row) + "]")
        return "\n".join(rows_str)

    def __getitem__(self, index):
        return self.data[index]

    def __add__(self, other: "Matrix") -> "Matrix":
        self._check_same_size(other)
        result = [
            [self.data[i][j] + other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return Matrix(result)

    def __sub__(self, other: "Matrix") -> "Matrix":
        self._check_same_size(other)
        result = [
            [self.data[i][j] - other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return Matrix(result)

    def __mul__(self, other: Union["Matrix", Vector, int, float]):
        if isinstance(other, (int, float)):
            return self.scalar_mul(other)
        if isinstance(other, Vector):
            return self.mat_vec_mul(other)
        if isinstance(other, Matrix):
            return self.mat_mul(other)
        raise TypeError("Tipo não suportado para mult.")

    def scalar_mul(self, scalar: float) -> "Matrix":
        result = [[x * scalar for x in row] for row in self.data]
        return Matrix(result)

    def mat_vec_mul(self, vec: Vector) -> Vector:
        if self.cols != vec.dim:
            raise ValueError("Dimensões impossiveis para multiplicação matriz-vetor")
        result = []
        for i in range(self.rows):
            s = sum(self.data[i][j] * vec.data[j] for j in range(self.cols))
            result.append(s)
        return Vector(result)

    def mat_mul(self, other: "Matrix") -> "Matrix":
        if self.cols != other.rows:
            raise ValueError("Dimensões impossiveis para multiplicação de matrizes")
        result = []
        for i in range(self.rows):
            row = []
            for j in range(other.cols):
                s = sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
                row.append(s)
            result.append(row)
        return Matrix(result)

    def transpose(self) -> "Matrix":
        result = [[self.data[j][i] for j in range(self.rows)] for i in range(self.cols)]
        return Matrix(result)

    def is_square(self) -> bool:
        return self.rows == self.cols

    def identity(n: int) -> "Matrix":
        data = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
        return Matrix(data)

    def copy(self) -> "Matrix":
        return Matrix([row[:] for row in self.data])

    def _check_same_size(self, other: "Matrix"):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrizes de tamanhos diferentes")
