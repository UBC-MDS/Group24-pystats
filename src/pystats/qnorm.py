def qnorm(p, mean=0, sd=1, lower_tail=True):
    """
    
    Quantile (Inverse Cumulative Distribution Function) of the normal distribution.

    Parameters
    ----------
    p: np.float64
        The probability for which to find the quantile.

    mean: np.float64, optional
        The mean (average) of the normal distribution. Default is 0.
        
    std_dev: np.float64, optional
        The standard deviation of the normal distribution. Default is 1.

    lower_tail: bool, optional
        If True, return the probability to the left of p in the normal distribution. 
        If False, return the probability to the right of p in the normal distribution.
        Default is True.
        
    Returns
    -------
    np.float64
        Returns the value of the inverse cumulative density function (cdf) of the normal distribution 
        given a certain random variable p, a population mean μ, and the population standard deviation σ.

    Formula
    -------
    
    If lower_tail=True:
        Q(p; μ, σ) = μ + σ * sqrt(2) * erfinv(2p - 1)
    
    If lower_tail=False:
        Q(p; μ, σ) = μ - σ * sqrt(2) * erfinv(2p - 1)

    The quantile represents the value below which a given proportion of the distribution
    falls. It is characterized by the mean (`μ`) and standard deviation (`σ`), determining
    the center and spread of the distribution.

    Example
    -------
    >>> qnorm(0.8413447460685429, mean=0, sd=1, lower_tail=True)
    1.0

    """