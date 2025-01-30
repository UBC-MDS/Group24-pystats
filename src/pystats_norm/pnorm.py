import numpy as np
from scipy.special import erf

def pnorm(q, mean=0, sd=1, lower_tail=True):
    """
    This function returns the value of the cumulative density function (cdf) of the 
    normal distribution with mean equal to `mean`, standard deviation equal to `sd`, 
    at a certain quantile q. 

    Parameters
    ----------
    q : np.float
        The quantile for which you want the `cdf` value.
    mean : np.float, optional
        The mean value of the normal distribution. Default is 0.
    sd : np.float, optional
        The standard deviation of the normal distribution. Default is 1.
    lower_tail : bool, optional
        If True, probabilities are P(X < q), otherwise, P(X > q). Default is True.

    Returns
    -------
    np.float64
        A probability value at the given quantile value of the specified cdf.

    Examples
    -------
    >>> pnorm(69, mean=60, sd=5, lower_tail=False)
    0.03593032
    """
    # Input type checks
    if not all(isinstance(param, (int, float)) for param in [q, mean, sd]):
        raise TypeError(f"Input parameters must be numerical")

    if not isinstance(lower_tail, bool):
        raise TypeError(f"Expected variable lower_tail to be boolean, got {type(lower_tail)}")

    # Value checks    
    if sd <= 0:
        raise ValueError("Standard deviation must be positive")
    
    if lower_tail:
        result = 1/2 * (1 + erf((q-mean)/(np.sqrt(2)*sd)))
        return result
    else:
        result = 1 - 1/2 * (1 + erf((q-mean)/(np.sqrt(2)*sd)))
        return result