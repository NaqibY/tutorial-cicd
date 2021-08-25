import main
import pytest


def test_sum_of_number():
    result = main.sum_of_number()
    # assert result==float
    assert type(result) == int
    assert result == 3


def test_myfunc():
    with pytest.raises(ValueError, match=r'.*123.*'):
        main.myfunc()
