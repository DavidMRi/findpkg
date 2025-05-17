import pytest
from findpkg.find import find
import math


def _linear_f(n):
    return n * 2


def _exponential_f(n):
    return 2 ** n


def _logarithmic_f(n):
    return math.log(n + 1)


def _hyperbolic_f(n):
    return math.sinh(n)


class TestFindFunction:

    # ---------- Valid Cases ----------

    @pytest.mark.parametrize("f,y,n", [(_linear_f, 34, 17),
                                       (_exponential_f, 256, 8),
                                       (_logarithmic_f,
                                        _logarithmic_f(87), 87),
                                       (_hyperbolic_f,
                                        _hyperbolic_f(79), 79)])
    def test_exact_match(self, f, y, n):
        assert find(f, y, 0, 100) == n

    @pytest.mark.parametrize("f,y", [(_linear_f, 34.56789),
                                     (_exponential_f, 1.2),
                                     (_logarithmic_f, 3.4),
                                     (_hyperbolic_f, 5.67)])
    def test_no_match(self, f, y):
        assert find(f, y, 0, 100) == -1

    @pytest.mark.parametrize("f,y,a,b", [(_linear_f, 20, 0, 9),
                                         (_exponential_f, 1024, 0, 9),
                                         (_logarithmic_f, 0, 1, 10),
                                         (_hyperbolic_f, 0, 1, 10)])
    def test_out_of_range(self, f, y, a, b):
        assert find(f, y, a, b) == -1

    @pytest.mark.parametrize("f,y", [(_linear_f, 0),
                                     (_exponential_f, 1),
                                     (_logarithmic_f, 0),
                                     (_hyperbolic_f, 0)])
    def test_match_at_lower_bound(self, f, y):
        assert find(f, y, 0, 100) == 0

    @pytest.mark.parametrize("f,y", [(_linear_f, 20),
                                     (_exponential_f, 1024),
                                     (_logarithmic_f, _logarithmic_f(10)),
                                     (_hyperbolic_f, _hyperbolic_f(10))])
    def test_match_at_upper_bound(self, f, y):
        assert find(f, y, 0, 10) == 10

    # ---------- Invalid Input Cases ----------

    def test_invalid_range_a_greater_than_b(self):
        with pytest.raises(AssertionError, match="Invalid range: b must be "
                                                 "equal or greater than a."):
            find(lambda x: x, 2.2, 5, 4)

    @pytest.mark.parametrize("a,b", [(-1, 0), (-2, -1)])
    def test_negative_range_values(self, a, b):
        with pytest.raises(AssertionError, match="Invalid range: a and b "
                                                 "must be non-negative."):
            find(lambda x: x, 2.2, a, b)

    def test_non_increasing_function(self):
        with pytest.raises(AssertionError, match="Invalid function: f is not"
                                                 " an increasing function"):
            find(lambda x: 10 - x, 2.2, 0, 4)

