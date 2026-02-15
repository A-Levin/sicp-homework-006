import pytest
from aggregation import sum_list, product_list, max_list, min_list, average

class TestSumList:
    def test_basic(self):
        assert sum_list([1, 2, 3, 4]) == 10
    def test_single(self):
        assert sum_list([5]) == 5
    def test_empty(self):
        assert sum_list([]) == 0
    def test_negative(self):
        assert sum_list([-1, -2, 3]) == 0

class TestProductList:
    def test_basic(self):
        assert product_list([1, 2, 3, 4]) == 24
    def test_single(self):
        assert product_list([5]) == 5
    def test_with_zero(self):
        assert product_list([1, 2, 0, 4]) == 0
    def test_empty(self):
        assert product_list([]) == 1

class TestMaxList:
    def test_basic(self):
        assert max_list([3, 1, 4, 1, 5]) == 5
    def test_single(self):
        assert max_list([42]) == 42
    def test_negative(self):
        assert max_list([-5, -2, -8]) == -2
    def test_first_is_max(self):
        assert max_list([9, 1, 2]) == 9

class TestMinList:
    def test_basic(self):
        assert min_list([3, 1, 4, 1, 5]) == 1
    def test_single(self):
        assert min_list([42]) == 42
    def test_negative(self):
        assert min_list([-5, -2, -8]) == -8
    def test_last_is_min(self):
        assert min_list([9, 5, 2]) == 2

class TestAverage:
    def test_basic(self):
        assert average([10, 20, 30]) == 20.0
    def test_single(self):
        assert average([5]) == 5.0
    def test_float_result(self):
        assert average([1, 2]) == 1.5
