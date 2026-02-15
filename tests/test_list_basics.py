import pytest
from list_basics import first, last, rest, init

class TestFirst:
    def test_single(self):
        assert first([1]) == 1
    def test_multiple(self):
        assert first([1, 2, 3]) == 1
    def test_strings(self):
        assert first(['a', 'b', 'c']) == 'a'

class TestLast:
    def test_single(self):
        assert last([1]) == 1
    def test_multiple(self):
        assert last([1, 2, 3]) == 3
    def test_strings(self):
        assert last(['a', 'b', 'c']) == 'c'

class TestRest:
    def test_multiple(self):
        assert rest([1, 2, 3]) == [2, 3]
    def test_two(self):
        assert rest([1, 2]) == [2]
    def test_single(self):
        assert rest([1]) == []

class TestInit:
    def test_multiple(self):
        assert init([1, 2, 3]) == [1, 2]
    def test_two(self):
        assert init([1, 2]) == [1]
    def test_single(self):
        assert init([1]) == []
