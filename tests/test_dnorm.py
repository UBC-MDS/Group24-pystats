import pytest
import pandas as pd
import numpy as np
from pystats.dnorm import dnorm

def test_output_datatype():
    """
    Test if the function returns a DataFrame with correct structure.
    """
    result = dnorm(1.5, mean=2, sd=3)
    assert isinstance(result, pd.DataFrame), "Output should be a pandas DataFrame."
    assert 'x' in result.columns and 'PDF' in result.columns, "DataFrame should contain 'x' and 'PDF' columns."
    assert result.shape == (1, 2), "Output DataFrame should have one row and two columns."

def test_standard_normal_pdf():
    """
    Test the PDF value for standard normal distribution.
    """
    result = dnorm(0, mean=0, sd=1)
    assert np.isclose(result['PDF'].iloc[0], 0.39894, atol=1e-5), "PDF value is incorrect for standard normal distribution."

def test_non_standard_pdf():
    """
    Test the PDF value for a non-standard normal distribution.
    """
    result = dnorm(1.96, mean=0, sd=1)
    assert np.isclose(result['PDF'].iloc[0], 0.05844, atol=1e-5), "PDF value is incorrect for x=1.96, mean=0, sd=1."

def test_negative_sd():
    """
    Test that dnorm raises ValueError for negative standard deviation.
    """
    with pytest.raises(ValueError, match="Standard deviation `sd` must be positive."):
        dnorm(1, mean=0, sd=-1)

def test_zero_sd():
    """
    Test that dnorm raises ValueError for zero standard deviation.
    """
    with pytest.raises(ValueError, match="Standard deviation `sd` must be positive."):
        dnorm(1, mean=0, sd=0)

def test_invalid_x():
    """
    Test that dnorm raises TypeError for non-numerical x.
    """
    with pytest.raises(TypeError, match="Expected `x` to be float or int"):
        dnorm("hello", mean=0, sd=1)

def test_invalid_mean():
    """
    Test that dnorm raises TypeError for non-numerical mean.
    """
    with pytest.raises(TypeError, match="Expected `mean` to be float or int"):
        dnorm(1, mean="mean", sd=1)

def test_invalid_sd_type():
    """
    Test that dnorm raises TypeError for non-numerical standard deviation.
    """
    with pytest.raises(TypeError, match="Expected `sd` to be float or int"):
        dnorm(1, mean=0, sd="std")

def test_extreme_x_values():
    """
    Test the behavior of the function with extreme x values.
    """
    result = dnorm(1e10, mean=0, sd=1)
    assert np.isclose(result['PDF'].iloc[0], 0.0, atol=1e-15), "PDF value should be near 0 for extreme x values."

def test_extreme_mean_values():
    """
    Test the behavior of the function with extreme mean values.
    """
    result = dnorm(0, mean=1e10, sd=1)
    assert np.isclose(result['PDF'].iloc[0], 0.0, atol=1e-15), "PDF value should be near 0 for extreme mean values."

def test_extreme_sd_values():
    """
    Test the behavior of the function with extremely large standard deviation.
    """
    result = dnorm(0, mean=0, sd=1e10)
    # Adjust the tolerance to account for floating-point precision
    assert np.isclose(result['PDF'].iloc[0], 3.989e-11, atol=1e-9), "PDF value is incorrect for extreme standard deviation."

