import pytest
from algorithms import binary_search, merge_sorted, quicksort, is_sorted

class TestBinarySearch:
    def test_found_middle(self):
        assert binary_search([1, 3, 5, 7, 9], 5) == 2
    def test_found_first(self):
        assert binary_search([1, 3, 5, 7, 9], 1) == 0
    def test_found_last(self):
        assert binary_search([1, 3, 5, 7, 9], 9) == 4
    def test_not_found(self):
        assert binary_search([1, 3, 5, 7, 9], 4) == -1
    def test_empty(self):
        assert binary_search([], 1) == -1

class TestMergeSorted:
    def test_basic(self):
        assert merge_sorted([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    def test_one_empty(self):
        assert merge_sorted([1, 2, 3], []) == [1, 2, 3]
    def test_both_empty(self):
        assert merge_sorted([], []) == []
    def test_overlap(self):
        assert merge_sorted([1, 2], [2, 3]) == [1, 2, 2, 3]

class TestQuicksort:
    def test_basic(self):
        assert quicksort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]
    def test_sorted(self):
        assert quicksort([1, 2, 3]) == [1, 2, 3]
    def test_reverse(self):
        assert quicksort([3, 2, 1]) == [1, 2, 3]
    def test_empty(self):
        assert quicksort([]) == []
    def test_single(self):
        assert quicksort([42]) == [42]

class TestIsSorted:
    def test_sorted(self):
        assert is_sorted([1, 2, 3]) == True
    def test_not_sorted(self):
        assert is_sorted([1, 3, 2]) == False
    def test_empty(self):
        assert is_sorted([]) == True
    def test_single(self):
        assert is_sorted([1]) == True
    def test_equal(self):
        assert is_sorted([2, 2, 2]) == True
