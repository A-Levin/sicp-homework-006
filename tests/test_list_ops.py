import inspect
import list_ops
from list_ops import (count_item, reverse_list, flatten_once, chunk,
                      interleave, run_length_encode, rotate, deduplicate,
                      zip_lists, unzip)


def test_count_item():
    assert count_item([1, 2, 1, 3, 1], 1) == 3
    assert count_item([1, 2, 3], 9) == 0
    assert count_item([], 1) == 0


def test_reverse_list():
    assert reverse_list([1, 2, 3]) == [3, 2, 1]
    assert reverse_list([]) == []
    original = [1, 2, 3]
    reverse_list(original)
    assert original == [1, 2, 3]


def test_flatten_once():
    assert flatten_once([[1, 2], [3, 4], [5]]) == [1, 2, 3, 4, 5]
    assert flatten_once([[], [1], []]) == [1]
    assert flatten_once([]) == []


def test_chunk():
    assert chunk([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
    assert chunk([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]
    assert chunk([], 2) == []
    assert chunk([1], 3) == [[1]]


def test_interleave():
    assert interleave([1, 2, 3], ['a', 'b', 'c']) == [1, 'a', 2, 'b', 3, 'c']
    assert interleave([1, 2], ['a', 'b', 'c', 'd']) == [1, 'a', 2, 'b', 'c', 'd']
    assert interleave([], [1, 2]) == [1, 2]


def test_run_length_encode():
    assert run_length_encode(['a', 'a', 'a', 'b', 'b', 'c']) == [(3, 'a'), (2, 'b'), (1, 'c')]
    assert run_length_encode([1, 1, 2, 1]) == [(2, 1), (1, 2), (1, 1)]
    assert run_length_encode([]) == []


def test_rotate():
    assert rotate([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
    assert rotate([1, 2, 3, 4, 5], -1) == [2, 3, 4, 5, 1]
    assert rotate([1, 2, 3], 0) == [1, 2, 3]
    assert rotate([1, 2, 3], 3) == [1, 2, 3]


def test_deduplicate():
    assert deduplicate([1, 2, 1, 3, 2, 4]) == [1, 2, 3, 4]
    assert deduplicate([1, 1, 1]) == [1]
    assert deduplicate([]) == []
    assert deduplicate([1, 2, 3]) == [1, 2, 3]


def test_zip_lists():
    assert zip_lists([1, 2, 3], ['a', 'b', 'c']) == [(1, 'a'), (2, 'b'), (3, 'c')]
    assert zip_lists([1, 2], ['a', 'b', 'c']) == [(1, 'a'), (2, 'b')]
    assert zip_lists([], []) == []


def test_unzip():
    assert unzip([(1, 'a'), (2, 'b'), (3, 'c')]) == ([1, 2, 3], ['a', 'b', 'c'])
    assert unzip([]) == ([], [])


def test_no_forbidden():
    forbidden = ['reversed(', '.reverse(', 'zip(']
    fns = ['count_item', 'reverse_list', 'flatten_once', 'chunk',
           'interleave', 'run_length_encode', 'rotate', 'deduplicate',
           'zip_lists', 'unzip']
    for name in fns:
        src = inspect.getsource(getattr(list_ops, name))
        for pattern in forbidden:
            assert pattern not in src, (
                f"{name}: запрещено использовать '{pattern}'"
            )
