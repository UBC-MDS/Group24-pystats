from pystats.pnorm import pnorm
import pytest
import math

def test_output_datatype():
    """
    Tests whether function returns correct data type within the range [0, 1].
    """
    result = pnorm(2, mean=5, sd=1.5, lower_tail=False)
    assert isinstance(result, float), "Result is not a float"
    assert 0 <= result <= 1, "Result is outside of probability boundaries [0, 1]"

@pytest.mark.parametrize(
        "q, mean, sd, lower_tail, expected",
        [
            (2, 5, 1.5, False, 0.9772499),
            (0.95, 0, 1, True, 0.8289439),
            (780, 20, 600, True, 0.8973627),
            (780, 20, 600, True, 0.1026373),
            (0, 0, 1, True, 0.5)
        ]
)
def test_normal_cases(q, mean, sd, lower_tail, expected):
    """
    Tests multiple normal cases for inverse CDF (qnorm equivalent).
    """
    actual = pnorm(q, mean, sd, lower_tail)
    assert math.isclose(actual, expected, abs_tol=1e-6)


def test_wrong_inputs():
    """
    Tests input types 
    1. `q` should always be a float
    2. `mean` is a float
    3. `sd` should always be a float
    4. lower_tail should always be a boolean 
    """
    with pytest.raises(TypeError):
        pnorm("2", mean=5, sd=1.5, lower_tail=True)
        pnorm(2, mean=[5], sd=1.5, lower_tail=True)
        pnorm(2, mean=5, sd=1.5, lower_tail=True)
        pnorm(2, mean=5, sd="1.5", lower_tail=True)
        pnorm(2, mean=5, sd=1.5, lower_tail="True")

def test_wrong_input_range():
    """
    Test that `sd` is non-negative
    """
    with pytest.raises(ValueError):
        pnorm(2, mean=5, sd=-1, lower_tail=True)