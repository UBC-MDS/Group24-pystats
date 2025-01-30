import numpy as np

def rnorm(n, mean=0, sd=1):
    """
    This function generates an array of length n normally distributed 
    random variables with mean equal to the `mean` and sd equal to the `sd`. 

    Parameters
    ----------
    n : int
        The number of random variables to be simulated.
    mean : np.float64, optional
        The mean value of the normal distribution. Default is 0.
    sd : np.float64, optional
        The standard deviation of the normal distribution. Default is 1.
    
    Returns
    -------
    np.ndarray
        A array of length n containing normally distributed random variables 
        with mean equal to  `mean` and sd equal to `sd`. 

    Examples
    -------
    >>> rnorm(2, mean=5, sd=2)
    array([6.3245, 4.5983])
    """

    # Checking for invalid inputs
    if not isinstance(n, int):
        raise ValueError('n must be an integer!')
    if n<0:
        raise ValueError('n must be a positive integer!')
    if not isinstance(mean, (int, np.float64)):
        raise ValueError('The mean value must be a number!')
    if not isinstance(sd, (int, np.float64)):
        raise ValueError('The standard deviation value must be a number!')
    if sd<0:
        raise ValueError('The standard deviation must be a positive number!')
    
    # Return an empty array if n = 0 is passed
    if n == 0:
        return np.array([])
    
    # Applying Box-Muller Transform to return a random normal array. 
    u1 = np.random.rand(n // 2 + 1)
    u2 = np.random.rand(n // 2 + 1)

    z0 = np.sqrt(-2 * np.log(u1)) * np.cos(2 * np.pi * u2)  
    z1 = np.sqrt(-2 * np.log(u1)) * np.sin(2 * np.pi * u2) 
    z = np.concatenate((z0, z1))[:n]  

    # Scale and shift array to match sd and mean. 
    return mean + sd * z