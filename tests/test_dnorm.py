from pystats.dnorm import dnorm
import pytest
import pandas as pd
import numpy as np


def test_output_datatype_and_structure():
    """
    Test whether the function returns a DataFrame with the correct structure.
    """
    result = dnorm(1.5, mean=2, sd=3)
    assert isinstance(result, pd.DataFrame), "Output should be a pandas DataFrame."
    assert list(result.columns) == ['x', 'PDF'], "DataFrame should have 'x' and 'PDF' columns."
    assert result.shape == (1, 2), "Output should have one row and two columns."


def test_standard_and_nonstandard_pdf():
    """
    Test PDF values for standard and non-standard normal distributions.
    """
    # Standard normal
    result = dnorm(0, mean=0, sd=1)
    assert np.isclose(result['PDF'].iloc[0], 0.39894, atol=1e-5), "PDF value is incorrect for standard normal."

    # Non-standard normal
    result = dnorm(1.96, mean=0, sd=1)
    assert np.isclose(result['PDF'].iloc[0], 0.05844, atol=1e-5), "PDF value is incorrect for non-standard normal."


def test_invalid_inputs():
    """
    Test invalid inputs for `x`, `mean`, and `sd`.
    """
    # Invalid `sd`
    with pytest.raises(ValueError, match="Standard deviation `sd` must be positive."):
        dnorm(1, mean=0, sd=-1)

    with pytest.raises(ValueError, match="Standard deviation `sd` must be positive."):
        dnorm(1, mean=0, sd=0)

    # Non-numerical inputs
    with pytest.raises(TypeError, match="Expected `x` to be float or int"):
        dnorm("hello", mean=0, sd=1)

    with pytest.raises(TypeError, match="Expected `mean` to be float or int"):
        dnorm(1, mean="mean", sd=1)

    with pytest.raises(TypeError, match="Expected `sd` to be float or int"):
        dnorm(1, mean=0, sd="std")


def test_extreme_and_edge_cases():
    """
    Test extreme and edge cases for inputs.
    """
    # Very small standard deviation
    result = dnorm(0, mean=0, sd=1e-10)
    assert np.isclose(result['PDF'].iloc[0], 1 / (1e-10 * np.sqrt(2 * np.pi)), atol=1e-5)

    # Very large `x` value
    result = dnorm(1e10, mean=0, sd=1)
    assert np.isclose(result['PDF'].iloc[0], 0.0, atol=1e-15), "PDF should be near 0 for extreme x values."

    # Very large `mean` value
    result = dnorm(0, mean=1e10, sd=1)
    assert np.isclose(result['PDF'].iloc[0], 0.0, atol=1e-15), "PDF should be near 0 for extreme mean values."