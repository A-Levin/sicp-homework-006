import pytest
from list_search import find_index, count, contains

class TestFindIndex:
    def test_found_first(self):
        assert find_index([10, 20, 30], 10) == 0
    def test_found_middle(self):
        assert find_index([10, 20, 30], 20) == 1
    def test_found_last(self):
        assert find_index([10, 20, 30], 30) == 2
    def test_not_found(self):
        assert find_index([10, 20, 30], 99) == -1
    def test_duplicate(self):
        assert find_index([10, 20, 30, 20], 20) == 1

class TestCount:
    def test_none(self):
        assert count([1, 2, 3], 4) == 0
    def test_one(self):
        assert count([1, 2, 3], 2) == 1
    def test_multiple(self):
        assert count([1, 2, 1, 3, 1], 1) == 3
    def test_all_same(self):
        assert count([5, 5, 5], 5) == 3

class TestContains:
    def test_found(self):
        assert contains([1, 2, 3], 2) == True
    def test_not_found(self):
        assert contains([1, 2, 3], 4) == False
    def test_empty(self):
        assert contains([], 1) == False
