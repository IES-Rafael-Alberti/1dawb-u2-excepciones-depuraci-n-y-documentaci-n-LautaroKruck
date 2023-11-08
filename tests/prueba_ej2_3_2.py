import pytest
from src.ej2_3_2  import serieNum

@pytest.mark.parametrize(
    "input_num, expected",
    [
        (10, ),
        (0, "**Error** Número introducido no positivo o cero."),
        ("a", "**Error** Número introducido no válido"),
        (-10, "**Error** Número introducido no positivo o cero."),
    ]
)
def test_serie_numero(input_num, expected):
    assert serieNum(input_num) == expected


def test_serie_numero():
    with pytest.raises(Exception, ValueError):
        serieNum(10, )