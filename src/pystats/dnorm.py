# dnorm.py
def dnorm(x, mean=0, sd=1):
    """
    Calculates the Probability Density of the normal distribution at a given point 

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
       x      PDF
    0  1.96  0.058440

    >>> result_df = dnorm(1.96, mean=0, sd=1)
    >>> result_df
       x      PDF
    0  1.96  0.058440
    """
    pass  # Function implementation will be added in a future milestone
