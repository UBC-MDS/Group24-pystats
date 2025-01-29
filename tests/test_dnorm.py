import pytest
import pandas as pd
import numpy as np
from pystats.dnorm import dnorm

@pytest.mark.parametrize(
    "x, mean, sd, expected_pdf, tolerance",
    [
        (0, 0, 1, 0.39894, 1e-5),  # Standard normal distribution
        (1.96, 0, 1, 0.05844, 1e-5),  # Non-standard case
        (1e10, 0, 1, 0.0, 1e-15),  # Extreme x values
        (0, 1e10, 1, 0.0, 1e-15),  # Extreme mean values
        (0, 0, 1e10, 3.989e-11, 1e-9),  # Extreme standard deviation
    ]
)
def test_pdf_values(x, mean, sd, expected_pdf, tolerance):
    """
    Test PDF values for different x, mean, and standard deviation values.
    """
    result = dnorm(x, mean=mean, sd=sd)
    assert np.isclose(result['PDF'].iloc[0], expected_pdf, atol=tolerance), \
        f"PDF value incorrect for x={x}, mean={mean}, sd={sd}."

@pytest.mark.parametrize(
    "sd",
    [-1, 0]  # Invalid standard deviation values
)
def test_invalid_sd(sd):
    """
    Test that dnorm raises ValueError for non-positive standard deviation.
    """
    with pytest.raises(ValueError, match="Standard deviation `sd` must be positive."):
        dnorm(1, mean=0, sd=sd)

@pytest.mark.parametrize(
    "x, mean, sd, expected_error, error_message",
    [
        ("hello", 0, 1, TypeError, "Expected `x` to be float or int"),
        (1, "mean", 1, TypeError, "Expected `mean` to be float or int"),
        (1, 0, "std", TypeError, "Expected `sd` to be float or int"),
    ]
)
def test_invalid_inputs(x, mean, sd, expected_error, error_message):
    """
    Test that dnorm raises TypeError for non-numerical inputs.
    """
    with pytest.raises(expected_error, match=error_message):
        dnorm(x, mean=mean, sd=sd)

@pytest.mark.parametrize(
    "x, mean, sd",
    [(1.5, 2, 3), (0, 0, 1), (-2, -1, 2)]
)
def test_output_structure(x, mean, sd):
    """
    Test if the function returns a DataFrame with correct structure for various inputs.
    """
    result = dnorm(x, mean=mean, sd=sd)
    assert isinstance(result, pd.DataFrame), "Output should be a pandas DataFrame."
    assert 'x' in result.columns and 'PDF' in result.columns, "DataFrame should contain 'x' and 'PDF' columns."
    assert result.shape == (1, 2), "Output DataFrame should have one row and two columns."
