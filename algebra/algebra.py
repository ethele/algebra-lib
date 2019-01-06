class Algebra:

    def __init__(self):
        return

    def simplify(self, expression):
        builder = ExpressionTreeBuilder()
        builder.expression = expression
        expression_tree = builder.build_tree()
        return str(expression_tree)

class ExpressionTreeBuilder:

    def __init__(self):
        self.expression = ""
        self.root = None

    def build_tree(self):
        binary_operators = "+"
        nodes_list = str.split(self.expression)
        print (nodes_list)
        for node in nodes_list:
            if self.root is None:
                print("Making new root")
                #self.root = ExpressionNode(node)
            elif node in binary_operators:
                print("Making new binary node")
        self.root = ExpressionNode(self.expression)
        return self.root

    def get_simplified_tree(self):
        return self.root

# class ExpressionTree:

class ExpressionNode:

    def __init__(self, expression):
        self.value = expression

    def __str__(self):
        return self.value
