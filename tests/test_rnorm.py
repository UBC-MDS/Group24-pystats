from pystats.rnorm import rnorm
import pytest
import numpy as np

def test_empty_n():
    """
    Tests whether the mean returned by the function is 0 and sd is 1. 
    """
    result = rnorm(0)
    assert result.size == 0, "An empty array of size 0 will be returned when n=0"

def test_standard_normal():
    """
    Tests whether the mean returned by the function is 0 and sd is 1. 
    """
    result = rnorm(2000)
    assert np.allclose(np.mean(result), 0, atol=0.5), "Mean should be close to 0"
    assert np.allclose(np.std(result), 1, atol=0.5), "Standard deviation should be close to 1"

def test_normal_mean5():
    """Tests whether the mean returned by the function is exactly 5 since the standard deviation is zero. 
    """
    result = rnorm(2000, 5, 0)
    assert np.all(result == 5), "All values should equal the mean when sd=0"

def test_sd_5():
    """Tests whether the mean is zero and standard deviation returned is close to 5.
    """
    result = rnorm(2000, 0, 5)
    assert np.allclose(np.mean(result), 0, atol=0.5), "Mean should be close to 0"
    assert np.allclose(np.std(result), 5, atol=0.5), "Standard deviation should be close to 5"

def test_sd5_mean10():
    """Tests whether the mean is closet to ten and standard deviation returned is close to 5.
    """
    result = rnorm(2000, 10, 5)
    assert np.allclose(np.mean(result), 10, atol=0.5), "Mean should be close to 10"
    assert np.allclose(np.std(result), 5, atol=0.5), "Standard deviation should be close to 5"

def test_invalid_n():
    """Tests that rnorm raises a value error when n is invalid.
    """
    with pytest.raises(ValueError, match='n must be an integer!'):
        rnorm('hello')
    
    with pytest.raises(ValueError, match='n must be positive integer!'):
        rnorm(-600)
    
def test_invalid_sd():
    """Tests that rnorm raises a value error when sd is invalid.
    """
    with pytest.raises(ValueError, match='sd must be a positive number!'):
        rnorm(1, 0, -50)

    with pytest.raises(ValueError, match='the sd value must be a number!'):
        rnorm(1, 0, 'hello')

def test_negative_mean():
    """Tests that rnorm raises a value error when mean is not a number.
    """
    with pytest.raises(ValueError, match='the mean value must be a number!'):
        rnorm(1, 'hello', 1)