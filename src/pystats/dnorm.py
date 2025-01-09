# dnorm.py
def dnorm(x, mean=0, sd=1):
    """
    Calculates the Probability Density of the normal distribution at a given point and optionally plots the PDF.

    Parameters
    ----------
    x : float
        The point at which to evaluate the PDF.
    mean : float, optional
        The mean (average) of the normal distribution. Default is 0.
    sd : float, optional
        The standard deviation of the normal distribution. Default is 1.
    graph : bool, optional
        Whether to plot the PDF graph. Default is True.

    Returns
    -------
    result_df : pandas.DataFrame
        A DataFrame containing the input value and the corresponding PDF value.
    result_graph : altair.Chart (optional)
        An Altair Chart object visualizing the PDF with a marker at the specified x-value.
        Returned only if `graph` is True.

    Raises
    ------
    ValueError
        If `sd` is zero or negative, as the standard deviation must be a positive number.
    TypeError
        If any of the input parameters (`x`, `mean`, `sd`) are not numerical.

    Example
    -------
    >>> dnorm(1.96, mean=0, sd=1, graph=False)
       x      PDF
    0  1.96  0.058440

    >>> result_df, result_graph = dnorm(1.96, mean=0, sd=1, graph=True)
    >>> result_df
       x      PDF
    0  1.96  0.058440
    >>> result_graph
    # Displays the PDF plot with a marker at x=1.96
    """
    pass  # Function implementation will be added in a future milestone
