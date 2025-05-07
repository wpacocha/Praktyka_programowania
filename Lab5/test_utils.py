import pytest
import utils


@pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (2, 3, 5), (3, 4, 7)])
def test_add(a, b, expected):
    assert utils.add(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [(5, 2, 3), (2, 1, 1), (10, 5, 5)])
def test_subtract(a, b, expected):
    assert utils.subtract(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [(1, 2, 2), (2, 3, 6), (4, 5, 20)])
def test_multiply(a, b, expected):
    assert utils.multiply(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [(4, 2, 2.0), (9, 3, 3.0)])
def test_divide(a, b, expected):
    assert utils.divide(a, b) == expected


import pytest
from utils import to_binary


@pytest.mark.parametrize(
    "num, expected", [(0, "0"), (1, "1"), (2, "10"), (10, "1010"), (100, "1100100")]
)
def test_to_binary_valid(num, expected):
    assert to_binary(num) == expected


@pytest.mark.parametrize("num", [-1, 101, 999])
def test_to_binary_out_of_range(num):
    with pytest.raises(ValueError):
        to_binary(num)


@pytest.mark.parametrize("num", [3.5, "12", None])
def test_to_binary_invalid_type(num):
    with pytest.raises(TypeError):
        to_binary(num)
