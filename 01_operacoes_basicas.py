from src.vector import Vector
from src.matrix import Matrix

print("=== Vetores ===")
v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])

print("v1 + v2 =", v1 + v2)
print("v1 · v2 =", v1.dot(v2))
print("||v1|| =", v1.norm())
print("Ângulo (rad) =", v1.angle(v2))

print("\n=== Matrizes ===")
A = Matrix([
    [1, 2],
    [3, 4]
])
B = Matrix([
    [5, 6],
    [7, 8]
])

print("A + B =")
print(A + B)
print("\nA * B =")
print(A * B)
print("\nA^T =")
print(A.transpose())
