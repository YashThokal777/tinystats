from tinystats import mean, median
import pytest


def test_mean():
    assert mean([1, 2, 3]) == 2


def test_mean_empty():
    with pytest.raises(ValueError, match="at least one data point"):
        mean([])


def test_median_odd():
    assert median([3, 1, 2]) == 2


def test_median_even():
    assert median([4, 1, 3, 2]) == 2.5
