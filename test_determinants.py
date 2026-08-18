import pytest
from src.matrix import Matrix
from src.determinants import determinant, inverse

def test_determinant_2x2():
    A = Matrix([[4, 7], [2, 6]])
    assert determinant(A) == pytest.approx(10.0)

def test_determinant_3x3():
    A = Matrix([
        [6, 1, 1],
        [4, -2, 5],
        [2, 8, 7]
    ])
    assert determinant(A) == pytest.approx(-306.0)

def test_determinant_identity():
    I = Matrix.identity(4)
    assert determinant(I) == pytest.approx(1.0)

def test_determinant_singular():
    A = Matrix([[1, 2], [2, 4]])
    assert determinant(A) == pytest.approx(0.0)

def test_inverse_2x2():
    A = Matrix([[4, 7], [2, 6]])
    A_inv = inverse(A)
    # Verificação: A * A⁻¹ ≈ I
    product = A * A_inv
    assert product.data[0][0] == pytest.approx(1.0)
    assert product.data[0][1] == pytest.approx(0.0)
    assert product.data[1][0] == pytest.approx(0.0)
    assert product.data[1][1] == pytest.approx(1.0)

def test_inverse_singular_raises():
    A = Matrix([[1, 2], [2, 4]])
    with pytest.raises(ValueError):
        inverse(A)
