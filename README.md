[![Documentation Status](https://readthedocs.org/projects/pystats-norm/badge/?version=latest)](https://pystats-norm.readthedocs.io/en/latest/?badge=latest)
[![codecov](https://codecov.io/github/UBC-MDS/Group24-pystats/graph/badge.svg?token=YqaFvm1hzi)](https://codecov.io/github/UBC-MDS/Group24-pystats)
![ci-cd](https://github.com/UBC-MDS/Group24-pystats/actions/workflows/ci-cd.yml/badge.svg)

# pystats_norm

<a href="https://github.com/UBC-MDS/Group24-pystats">
  <img src="https://github.com/UBC-MDS/Group24-pystats/blob/main/assets/pystat_logo.png" alt="App Platform" width="200">
</a>

`pystats_norm` is a lightweight statistical package that performs normal distributions calculations. Inspired by the simplicity and functionality of statistical tools in base R, `pystats_norm` provides a focused set of functions for generating random samples, calculating cumulative probabilities, determining quantiles, and evaluating probability density functions. This package hopes to serve statisticians, data scientists, and researchers looking to derive meaningful insights from their data.

It features the following core functions:
1. `rnorm`: Generate random samples from a normal distribution
2. `pnorm`: Compute probabilities for a given quantile (cumulative distribution function)
3. `qnorm`: Calculate the quantile (inverse of cumulative distribution function) for a given probability
4. `dnorm`: Evaluate the probability density function.

## Contributors
The members of the `pystats_norm` team are:
- Sarah Eshafi
- Jason Lee
- Abdul Safdar
- Rong Wan

## Installation

To use `pystats_norm`, please follow these instructions:

### 1. Install the package

In your terminal, type the following:

```bash
$ pip install pystats_norm
```

### 2. Import the functions

In your favourite Python IDE, you can import the `pystats_norm` functions as follows:

```python
>>> from pystats_norm.pnorm import pnorm
>>> from pystats_norm.dnorm import dnorm
>>> from pystats_norm.qnorm import qnorm
>>> from pystats_norm.rnorm import rnorm
```

You can now use the functions in your Python IDE!

## Functions

### `rnorm(n, mean=0, sd=1)`:  
Generates a NumPy array of length `n` containing normally distributed random variables with mean equal to  `mean` and sd equal to `sd`.

### `pnorm(q, mean=0, sd=1, lower_tail=True)`:  
Computes the cumulative distribution function (CDF) for a given quantile.

### `qnorm(p, mean=0, sd=1, lower_tail=True)`:  
Computes the quantile (inverse CDF) for a given probability.

### `dnorm(x, mean=0, sd=1)`:  
Calculates the Probability Density of the normal distribution for a given value

## Python Ecosystem Integration
`pystats_norm` is designed as a lightweight and intuitive package for normal distribution calculations. While similar functionality exists in libraries such as **SciPy** and **NumPy**, `pystats_norm` focuses exclusively on normal distributions, offering simplified functions with user-friendly syntax designed for statistical analysis. By providing well-documented and focused functionality, it serves as a niche yet essential tool in the Python ecosystem.

### Related Packages:
- [numpy.random.normal](https://numpy.org/doc/2.1/reference/random/generated/numpy.random.normal.html) - Generates random samples from a normal distribution.
- [scipy.stats.norm](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html) - PDF and CDF calculations for normal distributions.

## Usage & Documentation
For full documentation, please visit our [documentation site](https://pystats-norm.readthedocs.io/en/latest/).

## Contributing

Interested in contributing? Check out the [contributing guidelines](https://pystats-norm.readthedocs.io/en/latest/contributing.html). Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`pystats_norm` was created by Sarah Eshafi, Jason Lee, Abdul Safdar, Rong Wan. It is licensed under the terms of the MIT license.

## Credits

`pystats_norm` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
