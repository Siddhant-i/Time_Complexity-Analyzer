import ast


def check_conditions(code):
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return []

    conditions = []

    for node in ast.walk(tree):
        if isinstance(node, ast.If):
            conditions.append({
                "type": "if",
                "line": node.lineno
            })

            if node.orelse:
                is_elif = (len(node.orelse) == 1 and isinstance(node.orelse[0], ast.If))

                conditions.append({
                    "type": "elif" if is_elif else "else",
                    "line": node.orelse[0].lineno
                })

    return conditions
