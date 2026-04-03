from interval import interval, lower, upper, width, contains, overlaps, intersection
import inspect

def test_basic():
    i = interval(2, 5)
    assert lower(i) == 2
    assert upper(i) == 5

def test_width():
    assert width(interval(2, 5)) == 3
    assert width(interval(0, 0)) == 0

def test_contains():
    i = interval(2, 5)
    assert contains(i, 3)
    assert contains(i, 2)
    assert contains(i, 5)
    assert not contains(i, 6)
    assert not contains(i, 1)

def test_overlaps():
    assert overlaps(interval(1, 4), interval(3, 7))
    assert not overlaps(interval(1, 3), interval(4, 7))
    assert overlaps(interval(1, 5), interval(5, 9))  # граница

def test_intersection():
    result = intersection(interval(1, 4), interval(3, 7))
    assert lower(result) == 3
    assert upper(result) == 4
    assert intersection(interval(1, 3), interval(4, 7)) is None

def test_abstraction_barrier():
    for fn_name in ['width', 'contains', 'overlaps', 'intersection']:
        src = inspect.getsource(globals()[fn_name] if fn_name in globals() else __import__('interval').__dict__[fn_name])
        assert '[0]' not in src and '[1]' not in src, \
            f"{fn_name} не должна обращаться к индексам напрямую — используй lower/upper"
