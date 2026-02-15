import pytest
from comprehension import squares, evens, positives, lengths, upper_all

class TestSquares:
    def test_five(self):
        assert squares(5) == [1, 4, 9, 16, 25]
    def test_one(self):
        assert squares(1) == [1]
    def test_three(self):
        assert squares(3) == [1, 4, 9]

class TestEvens:
    def test_mixed(self):
        assert evens([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
    def test_all_even(self):
        assert evens([2, 4, 6]) == [2, 4, 6]
    def test_no_even(self):
        assert evens([1, 3, 5]) == []
    def test_with_zero(self):
        assert evens([0, 1, 2]) == [0, 2]

class TestPositives:
    def test_mixed(self):
        assert positives([-1, 2, -3, 4, 0]) == [2, 4]
    def test_all_positive(self):
        assert positives([1, 2, 3]) == [1, 2, 3]
    def test_all_negative(self):
        assert positives([-1, -2, -3]) == []

class TestLengths:
    def test_basic(self):
        assert lengths(['hi', 'hello', 'hey']) == [2, 5, 3]
    def test_empty_string(self):
        assert lengths(['', 'a', 'ab']) == [0, 1, 2]
    def test_single(self):
        assert lengths(['word']) == [4]

class TestUpperAll:
    def test_basic(self):
        assert upper_all(['hi', 'there']) == ['HI', 'THERE']
    def test_mixed_case(self):
        assert upper_all(['HeLLo', 'WoRLd']) == ['HELLO', 'WORLD']
    def test_empty(self):
        assert upper_all([]) == []
