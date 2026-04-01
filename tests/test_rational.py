from rational import rational, numer, denom, add_rational, mul_rational, equal_rational, print_rational
import inspect

def test_rational_basic():
    half = rational(1, 2)
    assert numer(half) == 1
    assert denom(half) == 2

def test_rational_reduces():
    r = rational(2, 4)
    assert numer(r) == 1
    assert denom(r) == 2

def test_add_rational():
    half = rational(1, 2)
    third = rational(1, 3)
    result = add_rational(half, third)
    assert numer(result) == 5
    assert denom(result) == 6

def test_add_rational_same():
    third = rational(1, 3)
    result = add_rational(third, third)
    assert numer(result) == 2
    assert denom(result) == 3

def test_mul_rational():
    half = rational(1, 2)
    third = rational(1, 3)
    result = mul_rational(half, third)
    assert numer(result) == 1
    assert denom(result) == 6

def test_equal_rational():
    assert equal_rational(rational(1, 2), rational(2, 4))
    assert not equal_rational(rational(1, 2), rational(1, 3))

def test_print_rational(capsys):
    print_rational(rational(1, 2))
    captured = capsys.readouterr()
    assert captured.out.strip() == "1/2"

def test_abstraction_barrier():
    import rational as r
    for fn_name in ['add_rational', 'mul_rational', 'equal_rational']:
        src = inspect.getsource(getattr(r, fn_name))
        assert '[0]' not in src and '[1]' not in src, \
            f"{fn_name} не должна обращаться к индексам напрямую — используй numer/denom"
