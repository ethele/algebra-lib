from algebra import algebra

def test_dumb():
    assert True

def test_simplify_3():
    solver = algebra.Algebra()
    answer = solver.simplify("3")
    assert answer == "3"