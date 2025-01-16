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
def test_normal_cases(p, mean, sd, lower_tail, expected):
    """
    Tests multiple normal cases for inverse CDF (qnorm equivalent).
    """
    assert qnorm(p, mean, sd, lower_tail) == expected

@pytest.mark.parametrize(
        "p, mean, sd, lower_tail",
        [
            ("hello", 0, 1, True),
            (0.99, "hi", 1, True),
            (0.99, 0, "bye", True),
            (5, 0, 1, True),
            (-3, 0, 1, True),
            (0.99, 0, -1, False)
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

    if not isinstance(p, (float, int)):
        raise TypeError(f"Expected input to be float or int, got {type(p)}")

    if not isinstance(mean, (float, int)):
        raise TypeError(f"Expected input to be float or int, got {type(mean)}")
    
    if not isinstance(sd, (float, int)):
        raise TypeError(f"Expected input to be float or int, got {type(sd)}")

    if not isinstance(lower_tail, bool):
        raise TypeError(f"Expected input to be float or int, got {type(lower_tail)}")

    if p < 0 or p > 1: 
        with pytest.raises(ValueError, match="Parameter 'p' stands for probability and should always be a float between 0 and 1."):
            results = qnorm(p, mean, sd, lower_tail)

    if sd < 0:
        with pytest.raises(ValueError, match="Standard deviation cannot be negative"):
            results = qnorm(p, mean, sd, lower_tail)
