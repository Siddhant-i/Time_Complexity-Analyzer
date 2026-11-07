import ast
import builtins


def check_errors(code):
    if not code.strip():
        return [{"line": 1, "message": "Please enter some code."}]

    try:
        tree = ast.parse(code)
    except SyntaxError as error:
        return [{
            "line": error.lineno or 1,
            "message": error.msg
        }]

    # Collect names that are created or imported.
    known_names = set(dir(builtins))

    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            known_names.add(node.name)

            args = (
                node.args.posonlyargs
                + node.args.args
                + node.args.kwonlyargs
            )

            known_names.update(arg.arg for arg in args)

            if node.args.vararg:
                known_names.add(node.args.vararg.arg)

            if node.args.kwarg:
                known_names.add(node.args.kwarg.arg)

        elif isinstance(node, ast.ClassDef):
            known_names.add(node.name)

        elif isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store):
            known_names.add(node.id)

        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            for alias in node.names:
                known_names.add(
                    alias.asname or alias.name.split(".")[0]
                )

    errors = []

    for node in ast.walk(tree):
        if (
            isinstance(node, ast.Name)
            and isinstance(node.ctx, ast.Load)
            and node.id not in known_names
            and not node.id.startswith("__")
        ):
            errors.append({
                "line": node.lineno,
                "message": (
                    f"'{node.id}' may be undefined. "
                    "Check its spelling and where it is created."
                )
            })

    return errors