from mytest import square
import pytest

@pytest.fixture

def input_value():
    return 4

def test_square(input_value):
    assert square(input_value) == 16
# def test_square():
#     assert square(2) == 4.5
    # assert square(3) == 9
    # assert square(4) == 16
    # assert square(5) == 25