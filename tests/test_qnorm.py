from pystats.qnorm import qnorm
import pytest
import pandas as pd
from scipy.stats import norm

def test_output_datatype():
    """
    Tests whether function returns correct data type.
    """
    results = qnorm(0.7, mean=2, sd=3, lower_tail = True)
    assert isinstance(results, float)

@pytest.mark.parametrize(
        "p, mean, sd, lower_tail, expected",
        [
            (0.8413447460685429, 0, 1, True, 1.0),
            (0.95, 0, 1, True, norm.ppf(0.95)),
            (0.95, 0, 1, False, norm.isf(0.95)),
            (0.99, 0, 1, True, norm.ppf(0.99)),
            (0.99, 0, 1, False, norm.isf(0.99))
        ]
)
def test_normal_cases(p, mean, sd, lower_tail, expected, tol=1e-6):
    """
    Tests multiple normal cases for inverse CDF (qnorm equivalent).
    """
    assert abs(qnorm(p, mean, sd, lower_tail) - expected) <= tol

@pytest.mark.parametrize(
        "p, mean, sd, lower_tail",
        [
            ("hello", 0, 1, True),
            (0.99, "hi", 1, True),
            (0.99, 0, "bye", True),
            (0.99, 0, 1, 5)
        ]
)
def test_inputs(p, mean, sd, lower_tail):
    """
    Tests input types 
    1. `p` should always be a numeric value between 0 and 1
    2. `mean` is a numeric value
    3. `sd` should always be a non-negative numeric value
    4. lower_tail should always be a boolean 
    """

    with pytest.raises(TypeError):
        qnorm(p, mean, sd, lower_tail)

@pytest.mark.parametrize(
        "p, mean, sd, lower_tail",
        [
            (5, 0, 1, True),
            (-3, 0, 1, True),
            (0.99, 0, -1, False)
        ]
)
def test_value_range(p, mean, sd, lower_tail):
    """
    Test that input values are within valid ranges.
    1. `p` must be between 0 and 1 (exclusive)
    2. Standard deviation must be non-negative
    """

    with pytest.raises(ValueError):
        results = qnorm(p, mean, sd, lower_tail)
