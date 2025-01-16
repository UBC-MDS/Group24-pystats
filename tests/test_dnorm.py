import pytest
import pandas as pd
from pystats.dnorm import dnorm
def test_output_datatype():
    """
    Tests whether the function returns the correct output data type.
    """
    results = dnorm(1.5, mean=2, sd=3)
    assert isinstance(results, pd.DataFrame), "Output should be a pandas DataFrame."
    assert 'x' in results.columns and 'PDF' in results.columns, "DataFrame should contain 'x' and 'PDF' columns."
    assert results.shape == (1, 2), "Output DataFrame should have one row and two columns."

def test_df_results():
    """
    Tests whether the function correctly calculates the PDF value.
    """
    results = dnorm(0, mean=0, sd=1)
    assert results['x'].iloc[0] == 0, "The input value should match the 'x' column."
    assert round(results['PDF'].iloc[0], 5) == 0.39894, "PDF value is incorrect for standard normal distribution."

    results = dnorm(1.96, mean=0, sd=1)
    assert round(results['PDF'].iloc[0], 5) == 0.05844, "PDF value is incorrect for x=1.96, mean=0, sd=1."

def test_nonsensical_input():
    """
    Tests the function's behavior for invalid input values.
    """
    # Test for negative standard deviation
    with pytest.raises(ValueError) as excinfo:
        dnorm(1, mean=0, sd=-1)
    assert str(excinfo.value) == "Standard deviation `sd` must be positive."

    # Test for non-numerical input
    with pytest.raises(TypeError) as excinfo:
        dnorm("hello", mean=0, sd=1)
    assert str(excinfo.value) == "Expected `x` to be float or int, got <class 'str'>."

    with pytest.raises(TypeError) as excinfo:
        dnorm(1, mean="mean", sd=1)
    assert str(excinfo.value) == "Expected `mean` to be float or int, got <class 'str'>."

    with pytest.raises(TypeError) as excinfo:
        dnorm(1, mean=0, sd="std")
    assert str(excinfo.value) == "Expected `sd` to be float or int, got <class 'str'>."
