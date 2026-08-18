import pytest
import math
from src.vector import Vector

def test_create_vector():
    v = Vector([1, 2, 3])
    assert v.dim == 3
    assert v.data == [1.0, 2.0, 3.0]

def test_empty_vector_raises():
    with pytest.raises(ValueError):
        Vector([])

def test_addition():
    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5, 6])
    result = v1 + v2
    assert result.data == [5.0, 7.0, 9.0]

def test_subtraction():
    v1 = Vector([5, 7, 9])
    v2 = Vector([1, 2, 3])
    result = v1 - v2
    assert result.data == [4.0, 5.0, 6.0]

def test_scalar_multiplication():
    v = Vector([1, 2, 3])
    result = v * 3
    assert result.data == [3.0, 6.0, 9.0]
    result2 = 2 * v
    assert result2.data == [2.0, 4.0, 6.0]

def test_dot_product():
    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5, 6])
    assert v1.dot(v2) == 32.0

def test_norm():
    v = Vector([3, 4])
    assert v.norm() == pytest.approx(5.0)

def test_normalize():
    v = Vector([3, 4])
    unit = v.normalize()
    assert unit.norm() == pytest.approx(1.0)
    assert unit.data == pytest.approx([0.6, 0.8])

def test_normalize_zero_vector():
    v = Vector([0, 0, 0])
    with pytest.raises(ValueError):
        v.normalize()

def test_angle():
    v1 = Vector([1, 0])
    v2 = Vector([0, 1])
    assert v1.angle(v2) == pytest.approx(math.pi / 2)

def test_different_dimensions_raise():
    v1 = Vector([1, 2])
    v2 = Vector([1, 2, 3])
    with pytest.raises(ValueError):
        v1 + v2
    with pytest.raises(ValueError):
        v1.dot(v2)
