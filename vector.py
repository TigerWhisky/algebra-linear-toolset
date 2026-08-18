"""
Implementação de Vetores em Python
"""

from typing import List, Union
import math

class Vector:
    def __init__(self, data: List[float]):
        if not data:
            raise ValueError("Vector não pode estar vazio")
        self.data = [float(x) for x in data]
        self.dim = len(self.data)

    def __repr__(self):
        return f"Vector({self.data})"

    def __str__(self):
        return f"[{', '.join(f'{x:.4f}' for x in self.data)}]"

    def __len__(self):
        return self.dim

    def __getitem__(self, index):
        return self.data[index]

    def __add__(self, other: "Vector") -> "Vector":
        self._check_same_dim(other)
        return Vector([a + b for a, b in zip(self.data, other.data)])

    def __sub__(self, other: "Vector") -> "Vector":
        self._check_same_dim(other)
        return Vector([a - b for a, b in zip(self.data, other.data)])

    def __mul__(self, scalar: Union[int, float]) -> "Vector":
        return Vector([x * scalar for x in self.data])

    def __rmul__(self, scalar: Union[int, float]) -> "Vector":
        return self.__mul__(scalar)

    def __truediv__(self, scalar: Union[int, float]) -> "Vector":
        if scalar == 0:
            raise ZeroDivisionError("Divisão por zero")
        return Vector([x / scalar for x in self.data])

    def dot(self, other: "Vector") -> float:
        """Produto escalar"""
        self._check_same_dim(other)
        return sum(a * b for a, b in zip(self.data, other.data))

    def norm(self) -> float:
        """Norma euclidiana"""
        return math.sqrt(self.dot(self))

    def normalize(self) -> "Vector":
        """vetor unitário"""
        n = self.norm()
        if n == 0:
            raise ValueError("Não é possível vectores nulos")
        return self / n

    def angle(self, other: "Vector") -> float:
        """Ângulo (rad) entre dois vetores"""
        cos_theta = self.dot(other) / (self.norm() * other.norm())
        # Evitar erros de precisão
        cos_theta = max(min(cos_theta, 1.0), -1.0)
        return math.acos(cos_theta)

    def _check_same_dim(self, other: "Vector"):
        if self.dim != other.dim:
            raise ValueError(f"Dimensões diferentes: {self.dim} vs {other.dim}")
