import pytest
from src.ej2_3_2  import pedirNumero

@pytest.mark.parametrize(
    "input_num, expected",
    [
        (10, 4),
        (0, 5),
        ("a", 2),
        (-10, 44.711),
    ]
)
def test_pedir_numero(input_num, expected):
    assert pedirNumero(input_num) == expected


def test_pedir_numero():
    with pytest.raises(Exception, ValueError):
        pedirNumero(1200.456, 0)