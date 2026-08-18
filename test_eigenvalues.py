import pytest
from src.matrix import Matrix
from src.eigenvalues import power_method

def test_power_method_simple():
    # Matriz com valor próprio dominante = 3
    # A = [[2, 1], [1, 2]] → valores próprios 3 e 1
    A = Matrix([[2, 1], [1, 2]])
    eigenvalue, eigenvector = power_method(A, max_iter=500, tol=1e-10)

    assert eigenvalue == pytest.approx(3.0, abs=1e-5)
    # O vetor próprio correspondente a 3 é aproximadamente [1, 1] (normalizado)
    assert abs(eigenvector[0]) == pytest.approx(abs(eigenvector[1]), abs=1e-5)

def test_power_method_identity():
    I = Matrix.identity(3)
    eigenvalue, eigenvector = power_method(I, max_iter=100)
    assert eigenvalue == pytest.approx(1.0, abs=1e-6)

def test_non_square_raises():
    A = Matrix([[1, 2, 3], [4, 5, 6]])
    with pytest.raises(ValueError):
        power_method(A)
