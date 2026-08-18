from src.matrix import Matrix
from src.eigenvalues import power_method

A = Matrix([
    [2, 1],
    [1, 2]
])

print("Matriz A:")
print(A)

eigenvalue, eigenvector = power_method(A)

print(f"\nValor próprio dominante ≈ {eigenvalue:.6f}")
print(f"Vetor próprio ≈ {eigenvector}")
