from pystats.dnorm import dnorm
import pytest
import pandas as pd
import numpy as np

def test_output_datatype():
    """
    Tests whether the function returns the correct output data type.
    """
    result = dnorm(1.5, mean=2, sd=3)
    assert isinstance(result, pd.DataFrame), "Output should be a pandas DataFrame."
    assert 'x' in result.columns and 'PDF' in result.columns, "DataFrame should contain 'x' and 'PDF' columns."
    assert result.shape == (1, 2), "Output DataFrame should have one row and two columns."

def test_standard_normal_pdf():
    """
    Tests the PDF value for standard normal distribution.
    """
    result = dnorm(0, mean=0, sd=1)
    assert np.isclose(result['PDF'].iloc[0], 0.39894, atol=1e-5), "PDF value is incorrect for standard normal distribution."

def test_non_standard_pdf():
    """
    Tests the PDF value for a non-standard normal distribution.
    """
    result = dnorm(1.96, mean=0, sd=1)
    assert np.isclose(result['PDF'].iloc[0], 0.05844, atol=1e-5), "PDF value is incorrect for x=1.96, mean=0, sd=1."

def test_invalid_sd():
    """
    Tests that dnorm raises a ValueError for invalid standard deviation.
    """
    with pytest.raises(ValueError, match="Standard deviation `sd` must be positive."):
        dnorm(1, mean=0, sd=-1)

def test_invalid_inputs():
    """
    Tests that dnorm raises TypeError for non-numerical inputs.
    """
    with pytest.raises(TypeError, match="Expected `x` to be float or int"):
        dnorm("hello", mean=0, sd=1)
    
    with pytest.raises(TypeError, match="Expected `mean` to be float or int"):
        dnorm(1, mean="mean", sd=1)

    with pytest.raises(TypeError, match="Expected `sd` to be float or int"):
        dnorm(1, mean=0, sd="std")

def test_extreme_values():
    """
    Tests behavior with extreme x values.
    """
    result = dnorm(1e10, mean=0, sd=1)
    assert np.isclose(result['PDF'].iloc[0], 0.0, atol=1e-15), "PDF value should be near 0 for extreme x values."
