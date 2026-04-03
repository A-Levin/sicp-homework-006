from comprehension import (evens_only, long_words, pairs, unique_chars,
                           word_lengths, transpose, group_by,
                           all_triples, matrix_from_flat)
import inspect

def test_evens_only():
    assert evens_only([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
    assert evens_only([1, 3, 5]) == []

def test_long_words():
    assert long_words(["hi", "hello", "hey", "world"], 3) == ["hello", "world"]

def test_pairs():
    assert pairs(3) == [(0, 1), (0, 2), (1, 2)]
    assert pairs(0) == []

def test_unique_chars():
    assert unique_chars("banana") == {'b', 'a', 'n'}

def test_word_lengths():
    assert word_lengths(["hi", "hello"]) == {'hi': 2, 'hello': 5}

def test_transpose():
    assert transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]
    assert transpose([[1], [2], [3]]) == [[1, 2, 3]]

def test_group_by():
    result = group_by(lambda x: x % 2, [1, 2, 3, 4, 5])
    assert set(result[0]) == {2, 4}
    assert set(result[1]) == {1, 3, 5}

def test_all_triples():
    result = all_triples(4)
    assert (0, 1, 2) in result
    assert (0, 1, 3) in result
    assert (1, 2, 3) in result
    assert len(result) == 4  # C(4,3) = 4
    for i, j, k in result:
        assert i < j < k

def test_matrix_from_flat():
    assert matrix_from_flat([1,2,3,4,5,6], 3) == [[1,2,3],[4,5,6]]
    assert matrix_from_flat([1,2,3,4], 2) == [[1,2],[3,4]]

def test_one_liners():
    import comprehension as c
    fns = ['evens_only','long_words','pairs','unique_chars','word_lengths',
           'transpose','group_by','all_triples','matrix_from_flat']
    for name in fns:
        fn = getattr(c, name)
        src = inspect.getsource(fn)
        lines = [l.strip() for l in src.splitlines()
                 if l.strip() and not l.strip().startswith('def')
                 and not l.strip().startswith('"""')]
        assert len(lines) == 1, f"{name} должна быть одной строкой, найдено: {len(lines)}"
