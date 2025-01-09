# pystats

pystats is a statistical package that performs normal distributions calculations. This package hopes to serve statisticians, data scientists, and researchers looking to derive meaningful insights from their data.

It features the following functions:
1. rnorm
2. pnorm
3. qnorm
4. dnorm

## Installation

```bash
$ pip install pystats
```

## Usage

- **rnorm(n, mean=0, sd=1)**: Returns a NumPy array of length n containing normally distributed random variables with mean equal to  `mean` and sd equal to `sd`. 
- **pnorm(q, mean=0, sd=1, lower_tail=True)**: Calculates a probability value at the given quantile value of the specified cdf.
- **qnorm(q, mean=0, sd=1, lower_tail=True)**: Calculates the value of the inverse cumulative density function (cdf) of the normal distribution. 
- **dnorm(x, mean=0, sd=1)**: Calculates the Probability Density of the normal distribution at a given point

## Contributors
The members of the `pystats` team are:
- Sarah Eshafi
- Jason Lee
- Abdul Safdar
- Rong Wan

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms. For more details refer to our Contributing.md file.

## License

`pystats` was created by Sarah Eshafi, Jason Lee, Abdul Safdar, Rong Wan. It is licensed under the terms of the MIT license.

## Credits

`pystats` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
