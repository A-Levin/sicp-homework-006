from list_ops import sum_list, max_list, count_item, reverse_list, flatten_once

def test_sum_list():
    assert sum_list([1, 2, 3, 4]) == 10
    assert sum_list([]) == 0
    assert sum_list([-1, 1]) == 0
    assert sum_list([5]) == 5

def test_max_list():
    assert max_list([3, 1, 4, 1, 5]) == 5
    assert max_list([-3, -1, -2]) == -1
    assert max_list([7]) == 7

def test_count_item():
    assert count_item([1, 2, 1, 3, 1], 1) == 3
    assert count_item([1, 2, 3], 9) == 0
    assert count_item([], 1) == 0
    assert count_item([1, 1, 1], 1) == 3

def test_reverse_list():
    assert reverse_list([1, 2, 3]) == [3, 2, 1]
    assert reverse_list([]) == []
    assert reverse_list([1]) == [1]
    original = [1, 2, 3]
    reverse_list(original)
    assert original == [1, 2, 3]

def test_flatten_once():
    assert flatten_once([[1, 2], [3, 4], [5]]) == [1, 2, 3, 4, 5]
    assert flatten_once([[], [1], []]) == [1]
    assert flatten_once([]) == []
