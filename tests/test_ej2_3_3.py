from typing import Literal
import pytest
from src.ej2_3_3  import serieNum

@pytest.mark.parametrize(
    "input_num, expected",
    [
        (10, '10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0'),
        (0, ''),
        (),
        (-10, ''),
    ]
)

def test_serieNum(input_num: int | Literal[10], expected: str | Literal['10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0'] ):
    assert serieNum(input_num) == expected

