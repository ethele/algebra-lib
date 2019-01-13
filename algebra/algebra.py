class Algebra:

    def __init__(self):
        return

    def simplify(self, expression):
        builder = ExpressionTreeBuilder()
        builder.expression = expression
        expression_tree = builder.build_tree()
        return str(expression_tree.simplify())

class ExpressionTreeBuilder:

    def __init__(self):
        self.expression = ""
        self.root = None
        self.node_list = []

    def build_tree(self):
        binary_operators = "+"
        if self.node_list == []:
            self.node_list = str.split(self.expression)
        print (self.node_list)
        node = self.node_list[0]
        if self.root is None:
            print("Making new root")
            self.root = ExpressionNode(node)
            try:
                self.node_list = self.node_list[1:]
                node = self.node_list[0]
            except IndexError:
                return self.root
        print("node is " + str(node))
        if node in binary_operators:
            print("Making new binary node for " + node)
            binary_node = BinaryNode(node)
            binary_node.left = self.root
            right_tree_builder = ExpressionTreeBuilder()
            right_tree_builder.node_list = self.node_list[1:]
            binary_node.right = right_tree_builder.build_tree()
            self.root = binary_node
        print ("root is " + str(self.root))
        return self.root

    def get_simplified_tree(self):
        return self.root



class ExpressionNode:

    def __init__(self, expression):
        self.value = expression

    def __str__(self):
        return self.value

    def simplify(self):
        return int(self.value)

class BinaryNode(ExpressionNode):

    def __init__(self, expression):
        self.value = expression
        self.left = None
        self.right = None

    def simplify(self):
        return self.left.simplify() + self.right.simplify()
    