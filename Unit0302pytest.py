from Unit0301pytest import add


def testAdd():
    assert add(10, 5) == 15
    assert add(10, 3) == 15
    assert add(1, 5) == 6
    assert add(3, 5) == 8
    assert add(-10, 5) == -5
