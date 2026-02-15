import pytest
from nested_lists import flatten, deep_sum, matrix_row, matrix_col, transpose

class TestFlatten:
    def test_basic(self):
        assert flatten([[1, 2], [3, 4], [5]]) == [1, 2, 3, 4, 5]
    def test_empty_inner(self):
        assert flatten([[], [1], []]) == [1]
    def test_single(self):
        assert flatten([[1, 2, 3]]) == [1, 2, 3]

class TestDeepSum:
    def test_flat(self):
        assert deep_sum([1, 2, 3]) == 6
    def test_nested(self):
        assert deep_sum([[1, 2], [3, 4]]) == 10
    def test_deep(self):
        assert deep_sum([[1, 2], [3, [4, 5]]]) == 15
    def test_empty(self):
        assert deep_sum([]) == 0

class TestMatrixRow:
    def test_first(self):
        m = [[1, 2, 3], [4, 5, 6]]
        assert matrix_row(m, 0) == [1, 2, 3]
    def test_second(self):
        m = [[1, 2, 3], [4, 5, 6]]
        assert matrix_row(m, 1) == [4, 5, 6]

class TestMatrixCol:
    def test_first(self):
        m = [[1, 2, 3], [4, 5, 6]]
        assert matrix_col(m, 0) == [1, 4]
    def test_middle(self):
        m = [[1, 2, 3], [4, 5, 6]]
        assert matrix_col(m, 1) == [2, 5]
    def test_last(self):
        m = [[1, 2, 3], [4, 5, 6]]
        assert matrix_col(m, 2) == [3, 6]

class TestTranspose:
    def test_square(self):
        assert transpose([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]
    def test_rectangular(self):
        assert transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]
