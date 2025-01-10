# pystats

**pystats** is a lightweight statistical package that performs normal distributions calculations. Inspired by the simplicity and functionality of statistical tools in base R, **pystats** provides a focused set of functions for generating random samples, calculating cumulative probabilities, determining quantiles, and evaluating probability density functions. This package hopes to serve statisticians, data scientists, and researchers looking to derive meaningful insights from their data.

It features the following core functions:
1. rnorm: Generate random samples from a normal distribution
2. pnorm: Compute probabilities for a given quantile (cumulative distribution function)
3. qnorm: Calculate the quantile (inverse of cumulative distribution function) for a given probability
4. dnorm: Evaluate the probability density function.

## Contributors
The members of the `pystats` team are:
- Sarah Eshafi
- Jason Lee
- Abdul Safdar
- Rong Wan

## Installation

```bash
$ pip install pystats
```

## Functions

**rnorm(n, mean=0, sd=1)**: 
Generates a NumPy array of length `n` containing normally distributed random variables with mean equal to  `mean` and sd equal to `sd`.

- **Parameters:**
  - `n` (int): Number of random samples to generate.
  - `mean` (float): Mean of the normal distribution (default: 0).
  - `sd` (float): Standard deviation of the normal distribution (default: 1).
- **Returns:** NumPy array of random samples.

**pnorm(q, mean=0, sd=1, lower_tail=True)**
Computes the cumulative distribution function (CDF) for a given quantile.

- **Parameters:**
  - `q` (float): Quantile value.
  - `mean` (float): Mean of the normal distribution (default: 0).
  - `sd` (float): Standard deviation of the normal distribution (default: 1).
  - `lower_tail` (bool): If `True`, returns \( P(X < q) \); if `False`, returns \( P(X > q) \) (default: `True`).
- **Returns:** Probability value.

**qnorm(q, mean=0, sd=1, lower_tail=True)**
Computes the quantile (inverse CDF) for a given probability.

- **Parameters:**
  - `q` (float): Probability value.
  - `mean` (float): Mean of the normal distribution (default: 0).
  - `sd` (float): Standard deviation of the normal distribution (default: 1).
  - `lower_tail` (bool): If `True`, returns the quantile for \( P(X < q) \); if `False`, returns the quantile for \( P(X > q) \) (default: `True`).
- **Returns:** Quantile value.

**dnorm(x, mean=0, sd=1)**
Calculates the Probability Density of the normal distribution for a given value

- **Parameters:**
  - `x` (float): Value at which to evaluate the PDF.
  - `mean` (float): Mean of the normal distribution (default: 0).
  - `sd` (float): Standard deviation of the normal distribution (default: 1).
- **Returns:** Probability density value.

## Python Ecosystem Integration
**pystats** is designed as a lightweight and intuitive package for normal distribution calculations. While similar functionality exists in libraries such as **SciPy** and **NumPy**, **pystats** focuses exclusively on normal distributions, offering simplified functions with user-friendly syntax designed for statistical analysis. By providing well-documented and focused functionality, it serves as a niche yet essential tool in the Python ecosystem.

### Related Packages:
- [numpy.random.normal] (https://numpy.org/doc/2.1/reference/random/generated/numpy.random.normal.html) - Generates random samples from a normal distribution.
- [scipy.stats.norm] (https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html) - PDF and CDF calculations for normal distributions.

## Usage
Work in progress. To be updated in a future release.

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms. For more details refer to our Contributing.md file.

## License

`pystats` was created by Sarah Eshafi, Jason Lee, Abdul Safdar, Rong Wan. It is licensed under the terms of the MIT license.

## Credits

`pystats` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
