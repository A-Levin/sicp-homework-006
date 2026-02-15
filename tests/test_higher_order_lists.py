import pytest
from higher_order_lists import apply_to_all, filter_by, reduce, count_if, all_satisfy, any_satisfy

class TestApplyToAll:
    def test_double(self):
        assert apply_to_all(lambda x: x * 2, [1, 2, 3]) == [2, 4, 6]
    def test_square(self):
        assert apply_to_all(lambda x: x ** 2, [1, 2, 3]) == [1, 4, 9]
    def test_empty(self):
        assert apply_to_all(lambda x: x, []) == []

class TestFilterBy:
    def test_positive(self):
        assert filter_by(lambda x: x > 0, [-1, 2, -3, 4]) == [2, 4]
    def test_even(self):
        assert filter_by(lambda x: x % 2 == 0, [1, 2, 3, 4]) == [2, 4]
    def test_none_match(self):
        assert filter_by(lambda x: x > 10, [1, 2, 3]) == []
    def test_all_match(self):
        assert filter_by(lambda x: x > 0, [1, 2, 3]) == [1, 2, 3]

class TestReduce:
    def test_sum(self):
        assert reduce(lambda a, b: a + b, [1, 2, 3, 4], 0) == 10
    def test_product(self):
        assert reduce(lambda a, b: a * b, [1, 2, 3, 4], 1) == 24
    def test_empty(self):
        assert reduce(lambda a, b: a + b, [], 0) == 0
    def test_string_concat(self):
        assert reduce(lambda a, b: a + b, ['a', 'b', 'c'], '') == 'abc'

class TestCountIf:
    def test_even(self):
        assert count_if(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]) == 3
    def test_positive(self):
        assert count_if(lambda x: x > 0, [-1, 2, -3, 4]) == 2
    def test_none(self):
        assert count_if(lambda x: x > 10, [1, 2, 3]) == 0

class TestAllSatisfy:
    def test_all_positive(self):
        assert all_satisfy(lambda x: x > 0, [1, 2, 3]) == True
    def test_not_all(self):
        assert all_satisfy(lambda x: x > 0, [1, -2, 3]) == False
    def test_empty(self):
        assert all_satisfy(lambda x: x > 0, []) == True

class TestAnySatisfy:
    def test_some_negative(self):
        assert any_satisfy(lambda x: x < 0, [1, -2, 3]) == True
    def test_none_negative(self):
        assert any_satisfy(lambda x: x < 0, [1, 2, 3]) == False
    def test_empty(self):
        assert any_satisfy(lambda x: x > 0, []) == False
