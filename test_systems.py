import pytest
from src.matrix import Matrix
from src.vector import Vector
from src.systems import solve_system, gauss_jordan, gaussian_elimination

def test_solve_simple_system():
    # 2x + y = 5
    # x + 3y = 5
    A = Matrix([[2, 1], [1, 3]])
    b = Vector([5, 5])
    x = solve_system(A, b)
    assert x.data == pytest.approx([2.0, 1.0])

def test_gauss_jordan():
    A = Matrix([[2, 1], [1, 3]])
    b = Vector([5, 5])
    x = gauss_jordan(A, b)
    assert x.data == pytest.approx([2.0, 1.0])

def test_known_system():
    # Sistema clássico
    A = Matrix([
        [2, 1, -1],
        [-3, -1, 2],
        [-2, 1, 2]
    ])
    b = Vector([8, -11, -3])
    x = solve_system(A, b)
    assert x.data == pytest.approx([2.0, 3.0, -1.0])

def test_singular_matrix_raises():
    A = Matrix([[1, 2], [2, 4]])  # singular
    b = Vector([3, 6])
    with pytest.raises(ValueError):
        solve_system(A, b)

def test_dimension_mismatch_raises():
    A = Matrix([[1, 2], [3, 4]])
    b = Vector([1, 2, 3])
    with pytest.raises(ValueError):
        solve_system(A, b)
