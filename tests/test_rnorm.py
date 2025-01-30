from pystats_norm.rnorm import rnorm
import pytest
import numpy as np

def test_empty_n():
    """
    Tests whether the mean returned by the function is 0 and sd is 1. 
    """
    result = rnorm(0)
    assert result.size == 0, "An empty array of size 0 will be returned when n=0"

@pytest.mark.parametrize(
    "n, mean, sd, expected_mean, expected_sd",
    [
        (2000, 0, 1, 0, 1),   # Standard normal distribution with mean = 0 and sd = 1
        (2000, 5, 0, 5, 0),   # All values generated should be 5 when sd = 0.
        (2000, 0, 5, 0, 5),   # mean = 0, sd = 5
        (2000, 10, 5, 10, 5)  # mean = 10 , sd = 5
    ]
)

def test_normal_cases(n, mean, sd, expected_mean, expected_sd):
    """Tests rnorm functions for normal cases."""
    result = rnorm(n, mean, sd)
    
    if sd == 0:
        assert np.all(result == expected_mean)
    else:
        assert np.allclose(np.mean(result), expected_mean, atol=0.5)
        assert np.allclose(np.std(result), expected_sd, atol=0.5)

@pytest.mark.parametrize(
        "n, mean, sd",
        [
            ("hello", 0, 1),
            (-600, 0, 1),
            (1, 0, -50),
            (1, 0, 'hello'),
            (1, 'hello', 1)
        ]
)

def test_invalid_types(n, mean, sd):
    """
    Tests input types 
    1.  `n` should always be an integer.
    2.  `n` must be a positive integer.
    3.  `sd` must be a positive number.
    4.  `sd` must always be a number.
    5.  `mean` value must be a number.
    """

    with pytest.raises(ValueError):
        rnorm(n, mean, sd)