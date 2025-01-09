def pnorm(q, mean=0, sd=1, lower_tail=True):
    """
    This function returns the value of the cumulative density function (cdf) of the 
    normal distribution with mean equal to `mean`, standard deviation equal to `sd`, 
    at a certain point q. 

    Parameters
    ----------
    q : float
        The number of random variables to be simulated.
    mean : float, optional
        The mean value of the normal distribution. Default is 0.
    sd : float, optional
        The standard deviation of the normal distribution. Default is 1.
    lower_tail : binary, optional
        If True, probabilities are P(X < q), otherwise, P(X > q). Default is True.

    Returns
    -------
    numpy.float64
        A probability value at the given quantile value of the specified cdf.

    Examples
    -------
    >>> pnorm(69, mean=60, sd=5, lower_tail=False)
    0.03593032
    """