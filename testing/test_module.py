'''
Ejemplo sencillo utilizando pytest
'''
from src import module

import pytest

@pytest.mark.parametrize("val1, val2, expected_result",[
    (5,5,10),
    (10,5,1),
])
def test_sum_two_value(val1, val2, expected_result):
    result = module.sum_two_values(val1,val2)

    assert result == expected_result