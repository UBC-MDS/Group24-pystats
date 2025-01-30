import numpy as np
from scipy.special import erfinv
import scipy.stats as stats
import math

def qnorm(p, mean=0, sd=1, lower_tail=True):
    """
    
    Quantile (Inverse Cumulative Distribution Function) of the normal distribution.

    Parameters
    ----------
    p: np.float64
        The probability for which to find the quantile. Must be between 0 and 1 (exclusive).

    mean: np.float64, optional
        The mean (average) of the normal distribution. Default is 0.
        
    sd: np.float64, optional
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

    # Input type checks
    if not all(isinstance(param, (int, float)) for param in [p, mean, sd]):
        raise TypeError(f"Input parameters must be numerical")

    if not isinstance(lower_tail, bool):
        raise TypeError(f"Expected input to be boolean, got {type(lower_tail)}")

    # Value checks
    if not 0 < p < 1:
        raise ValueError("p must be between 0 and 1 (exclusive).")
    
    if not sd > 0:
        raise ValueError("standard deviation must be non-negative")
    
    if lower_tail:
        result = mean + sd * np.sqrt(2) * erfinv(2 * p - 1)
        return result
    else:
        result = mean - sd * np.sqrt(2) * erfinv(2 * p - 1)
        return result