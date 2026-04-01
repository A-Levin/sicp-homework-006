from comprehension import squares, evens_only, long_words, pairs, unique_chars, word_lengths
import inspect

def test_squares():
    assert squares(5) == [1, 4, 9, 16, 25]
    assert squares(1) == [1]
    assert squares(0) == []

def test_evens_only():
    assert evens_only([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
    assert evens_only([1, 3, 5]) == []
    assert evens_only([]) == []

def test_long_words():
    assert long_words(["hi", "hello", "hey", "world"], 3) == ["hello", "world"]
    assert long_words(["a", "bb"], 5) == []

def test_pairs():
    assert pairs(3) == [(0, 1), (0, 2), (1, 2)]
    assert pairs(0) == []
    assert pairs(1) == []

def test_unique_chars():
    assert unique_chars("banana") == {'b', 'a', 'n'}
    assert unique_chars("aaa") == {'a'}
    assert unique_chars("") == set()

def test_word_lengths():
    assert word_lengths(["hi", "hello"]) == {'hi': 2, 'hello': 5}
    assert word_lengths([]) == {}

def test_one_liners():
    import comprehension as c
    for name in ['squares', 'evens_only', 'long_words', 'pairs', 'unique_chars', 'word_lengths']:
        fn = getattr(c, name)
        src = inspect.getsource(fn)
        lines = [l.strip() for l in src.splitlines()
                 if l.strip() and not l.strip().startswith('def')
                 and not l.strip().startswith('"""')]
        assert len(lines) == 1, f"{name} должна быть одной строкой, найдено: {len(lines)}"
