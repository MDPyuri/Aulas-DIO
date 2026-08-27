import pytest
from AAB_calculadora import somar, dividir


def test_somar():
    assert somar(2, 3) == 5


def test_dividir():
    assert dividir(10, 2) == 5


def test_dividir_por_zero():
    with pytest.raises(ValueError):
        dividir(10, 0)


@pytest.mark.parametrize(
    "a,b,resultado",
    [
        (1, 1, 2),
        (2, 3, 5),
        (-1, 1, 0),
        (10, 5, 15),
    ]
)
def test_somar_varios_casos(a, b, resultado):
    assert somar(a, b) == resultado