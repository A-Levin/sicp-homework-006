import pytest
from practical import unique, intersection, difference, zip_lists, unzip, group_by

class TestUnique:
    def test_basic(self):
        result = unique([1, 2, 2, 3, 1, 4])
        assert sorted(result) == [1, 2, 3, 4]
    def test_no_duplicates(self):
        assert unique([1, 2, 3]) == [1, 2, 3]
    def test_all_same(self):
        assert unique([5, 5, 5]) == [5]

class TestIntersection:
    def test_basic(self):
        result = intersection([1, 2, 3], [2, 3, 4])
        assert sorted(result) == [2, 3]
    def test_no_common(self):
        assert intersection([1, 2], [3, 4]) == []
    def test_all_common(self):
        result = intersection([1, 2], [1, 2])
        assert sorted(result) == [1, 2]

class TestDifference:
    def test_basic(self):
        result = difference([1, 2, 3], [2, 4])
        assert sorted(result) == [1, 3]
    def test_no_common(self):
        result = difference([1, 2], [3, 4])
        assert sorted(result) == [1, 2]
    def test_all_common(self):
        assert difference([1, 2], [1, 2]) == []

class TestZipLists:
    def test_basic(self):
        assert zip_lists([1, 2, 3], ['a', 'b', 'c']) == [(1, 'a'), (2, 'b'), (3, 'c')]
    def test_single(self):
        assert zip_lists([1], ['a']) == [(1, 'a')]
    def test_empty(self):
        assert zip_lists([], []) == []

class TestUnzip:
    def test_basic(self):
        assert unzip([(1, 'a'), (2, 'b')]) == ([1, 2], ['a', 'b'])
    def test_single(self):
        assert unzip([(1, 'a')]) == ([1], ['a'])
    def test_empty(self):
        assert unzip([]) == ([], [])

class TestGroupBy:
    def test_even_odd(self):
        result = group_by(lambda x: x % 2, [1, 2, 3, 4, 5])
        assert result == {0: [2, 4], 1: [1, 3, 5]}
    def test_first_char(self):
        result = group_by(lambda s: s[0], ['apple', 'ant', 'bear'])
        assert result == {'a': ['apple', 'ant'], 'b': ['bear']}
