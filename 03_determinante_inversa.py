from src.matrix import Matrix
from src.determinants import determinant, inverse

A = Matrix([
    [4, 7],
    [2, 6]
])

print("Matriz A:")
print(A)
print("\nDeterminante =", determinant(A))

A_inv = inverse(A)
print("\nInversa de A:")
print(A_inv)

print("\nVerificação A * A⁻¹ =")
print(A * A_inv)
