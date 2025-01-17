import numpy as np
import pandas as pd

def dnorm(x, mean=0, sd=1):
    """
    Calculates the Probability Density of the normal distribution at a given point.

    Parameters
    ----------
    x : float
        The point at which to evaluate the PDF.
    mean : float, optional
        The mean (average) of the normal distribution. Default is 0.
    sd : float, optional
        The standard deviation of the normal distribution. Default is 1.

    Returns
    -------
    result_df : pandas.DataFrame
        A DataFrame containing the input value and the corresponding PDF value.

    Raises
    ------
    ValueError
        If `sd` is zero or negative, as the standard deviation must be a positive number.
    TypeError
        If any of the input parameters (`x`, `mean`, `sd`) are not numerical.

    Example
    -------
    >>> dnorm(1.96, mean=0, sd=1)
           x       PDF
    0   1.96  0.058440

    >>> result_df = dnorm(1.96, mean=0, sd=1)
    >>> result_df
           x       PDF
    0   1.96  0.058440
    """
    
    # Input type checks
    if not isinstance(x, (float, int)):
        raise TypeError(f"Expected `x` to be float or int, got {type(x)}")
    
    if not isinstance(mean, (float, int)):
        raise TypeError(f"Expected `mean` to be float or int, got {type(mean)}")
    
    if not isinstance(sd, (float, int)):
        raise TypeError(f"Expected `sd` to be float or int, got {type(sd)}")
    
    # Value checks
    if sd <= 0:
        raise ValueError("Standard deviation `sd` must be positive.")
    
    # Calculate the PDF value
    pdf = (1 / (sd * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / sd) ** 2)
    
    # Create a DataFrame with the results
    result_df = pd.DataFrame({
        "x": [x],
        "PDF": [pdf]
    })
    
    return result_df

# # Example usage
# if __name__ == "__main__":
#     result = dnorm(1.96, mean=0, sd=1)
#     print(result)
