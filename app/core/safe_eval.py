import ast
import operator

OPS = {
    ast.Gt: operator.gt,
    ast.GtE: operator.ge,
    ast.Lt: operator.lt,
    ast.LtE: operator.le,
    ast.Eq: operator.eq,
    ast.NotEq: operator.ne,
    ast.In: lambda a, b: a in b
}

class SafeEvaluator(ast.NodeVisitor):
    def __init__(self, context):
        self.context = context

    def visit_Compare(self, node):
        left = self.visit(node.left)
        right = self.visit(node.comparators[0])
        op = OPS.get(type(node.ops[0]))

        if not op:
            raise ValueError('Operator not allowed')

        return op(left, right)

    def visit_Name(self, node):
        return self.context.get(node.id)

    def visit_Constant(self, node):
        return node.value

    def visit_List(self, node):
        return [self.visit(e) for e in node.elts]


def evaluate_condition(condition: str, attributes: dict) -> bool:
    tree = ast.parse(condition, mode='eval')
    return SafeEvaluator(attributes).visit(tree.body)
