from tuples import point, x_coord, y_coord, distance, midpoint, swap

def test_point():
    p = point(3, 4)
    assert x_coord(p) == 3
    assert y_coord(p) == 4

def test_point_zero():
    p = point(0, 0)
    assert x_coord(p) == 0
    assert y_coord(p) == 0

def test_distance():
    assert distance(point(0, 0), point(3, 4)) == 5.0
    assert distance(point(1, 1), point(1, 1)) == 0.0
    assert distance(point(0, 0), point(1, 0)) == 1.0

def test_midpoint():
    assert midpoint(point(0, 0), point(4, 2)) == (2.0, 1.0)
    assert midpoint(point(1, 1), point(3, 3)) == (2.0, 2.0)

def test_swap():
    assert swap((1, 2)) == (2, 1)
    assert swap(("a", "b")) == ("b", "a")
    assert swap((42, 0)) == (0, 42)
