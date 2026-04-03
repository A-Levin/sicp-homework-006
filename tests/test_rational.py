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
    result = add_rational(rational(1, 2), rational(1, 3))
    assert numer(result) == 5
    assert denom(result) == 6

def test_add_rational_reduces():
    result = add_rational(rational(1, 3), rational(1, 3))
    assert numer(result) == 2
    assert denom(result) == 3

def test_mul_rational():
    result = mul_rational(rational(1, 2), rational(1, 3))
    assert numer(result) == 1
    assert denom(result) == 6

def test_equal_rational():
    assert equal_rational(rational(1, 2), rational(2, 4))
    assert not equal_rational(rational(1, 2), rational(1, 3))

def test_print_rational(capsys):
    print_rational(rational(1, 2))
    assert capsys.readouterr().out.strip() == "1/2"

def test_abstraction_barrier():
    import rational as r
    for fn_name in ['add_rational', 'mul_rational', 'equal_rational']:
        src = inspect.getsource(getattr(r, fn_name))
        assert '[0]' not in src and '[1]' not in src, \
            f"{fn_name} не должна обращаться к индексам — используй numer/denom"
