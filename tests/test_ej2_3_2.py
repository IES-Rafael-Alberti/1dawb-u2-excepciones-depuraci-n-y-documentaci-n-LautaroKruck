from typing import Literal
import pytest
from src.ej2_3_2  import serieNum

@pytest.mark.parametrize(
    "input_num, expected",
    [
        (10, '1 , 3 , 5 , 7 , 9'),
        (0, ''),
        ("a", ''),
        (-10, ''),
    ]
)

def test_serieNum(input_num: int | Literal[10], expected: str | Literal['1 , 3 , 5 , 7 , 9'] ):
    assert serieNum(input_num) == expected

def test_serie_numeros():
    with pytest.raises(ValueError):
        serieNum("a")