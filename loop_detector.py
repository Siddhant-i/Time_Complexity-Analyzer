import ast

class LoopVisitor(ast.NodeVisitor):
    def __init__(self):
        self.loops = []

    def visit_For(self, node):
        self.loops.append({
            "type": "for",
            "line": node.lineno,
            "nested": False
        })

        self.generic_visit(node)

    def visit_While(self, node):
        self.loops.append({
            "type": "while",
            "line": node.lineno,
            "nested": False
        })

        self.generic_visit(node)


def detect_loops(code):
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return []

    visitor = LoopVisitor()
    visitor.visit(tree)

    # Mark a loop as nested when it contains another loop.
    for loop in visitor.loops:
        outer_line = loop["line"]

        outer_node = next(
            (
                node for node in ast.walk(tree)
                if isinstance(node, (ast.For, ast.While))
                and node.lineno == outer_line
            ),
            None
        )

        if outer_node:
            loop["nested"] = any(
                isinstance(child, (ast.For, ast.While))
                for statement in outer_node.body
                for child in ast.walk(statement)
            )

    return visitor.loops