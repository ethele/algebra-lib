from algebra import algebra

def test_dumb():
    assert True

def test_simplify_3():
    solver = algebra.Algebra()
    answer = solver.simplify("3")
    assert answer == "3"

# Next steps: Create interface ExpressionNode
# Create implementing classes ValueNode / UnaryExpressionNode 
# and BinaryExpressionNode
# Then when see binary operator, create new BinaryExpressionNode
# With 'root' on the left and a new expression tree (root node) to the right 
# generated from the remainder of the expression
# with a stored operator value for the node

# def test_add_two_digits():
#     solver = algebra.Algebra()
#     answer = solver.simplify("3 + 4")
#     assert answer == "7"