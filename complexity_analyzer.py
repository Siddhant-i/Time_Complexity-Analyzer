
import ast

def get_loop_step(node):

    if not isinstance(node, ast.While):
        return None

    for statement in ast.walk(node):

        if isinstance(statement, ast.AugAssign):
            if isinstance(statement.op, (ast.Mult, ast.FloorDiv)):
                return "logarithmic"

            if isinstance(statement.op, (ast.Add, ast.Sub)):
                return "linear"

        if isinstance(statement, ast.Assign):
            value = statement.value

            if isinstance(value, ast.BinOp):

                if isinstance(value.op, (ast.Mult, ast.FloorDiv)):
                    return "logarithmic"

                if isinstance(value.op, (ast.Add, ast.Sub)):
                    return "linear"

    return None

def get_range_bound(loop):
    if not isinstance(loop, ast.For):
        return None

    iterator = loop.iter

    if not isinstance(iterator, ast.Call):
        return None

    if not isinstance(iterator.func, ast.Name):
        return None

    if iterator.func.id != "range":
        return None
    if not iterator.args:
        return None

    return ast.unparse(iterator.args[0])


def get_nested_loops(tree):
    nested = []

    def visit(node, parents=None):

        if parents is None:
            parents = []

        current = list(parents)

        if isinstance(node, (ast.For, ast.While)):

            if current:
                nested.append((current[-1], node))

            current.append(node)

        for child in ast.iter_child_nodes(node):
            visit(child, current)

    visit(tree)
    return nested


def get_loop_depth(tree):

    maximum = 0

    def visit(node, depth=0):
        nonlocal maximum

        if isinstance(node, (ast.For, ast.While)):
            depth += 1
            maximum = max(maximum, depth)
        for child in ast.iter_child_nodes(node):
            visit(child, depth)

    visit(tree)

    return maximum

def contains_halving(node):

    for child in ast.walk(node):

        if isinstance(child, ast.BinOp):

            if isinstance(child.op, (ast.FloorDiv, ast.Div)):
                if isinstance(child.right, ast.Constant):
                    if isinstance(child.right.value, (int, float)):
                        if child.right.value > 1:
                            return True

    return False

def contains_slice(node):

    for child in ast.walk(node):

        if isinstance(child, ast.Subscript):

            if isinstance(child.slice, ast.Slice):
                return True
    return False


def contains_linear_change(node):

    for child in ast.walk(node):
        if isinstance(child, ast.BinOp):

            if isinstance(child.op, (ast.Add, ast.Sub)):

                if isinstance(child.right, ast.Constant):
                    return True

    return False

def analyze_recursion(tree):
    for function in ast.walk(tree):

        if not isinstance( function, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue

        calls = []

        for child in ast.walk(function):
            if child is not function and isinstance(
                child,
                (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda)):
                continue

            if isinstance(child, ast.Call):
                if (isinstance(child.func, ast.Name)
                    and child.func.id == function.name):
                    calls.append(child)

        if not calls:
            continue
        call_count = len(calls)

        has_loop = any(
            isinstance(child, (ast.For, ast.While))
            for child in ast.walk(function)
        )

        has_slice = contains_slice(function)
        has_halving = contains_halving(function)

        # if has_loop and has_slice and call_count >= 1:
        #     return "O(n * n!)"

        if call_count >= 2 and has_halving:
            return "O(n log n)"

        if call_count >= 2:
            return "O(2^n)"

        if call_count == 1:
            if contains_linear_change(calls[0]):
                return "O(n)"

        if call_count == 1 and has_halving:

            if has_loop:
                return "O(n log n)"
            
            return "O(log n)"

    return None

def analyze_complexity(code):
    try:
        tree = ast.parse(code)

    except SyntaxError:
        return {"complexity": "Cannot analyze"}

    recursion_result = analyze_recursion(tree)

    if recursion_result:
        return {"complexity": recursion_result}

    loops = [
        i for i in ast.walk(tree)
        if isinstance(i, (ast.For, ast.While))]

    if not loops:
        return {"complexity": "O(1)"}

    depth = get_loop_depth(tree)

    if depth > 3:
        return {"complexity": "Needs further analysis"}

    # Check three nested loops.
    if depth == 3:

        return {
            "complexity": "O(n^3)"
        }

    if depth == 2:

        nested = get_nested_loops(tree)
        for outer, inner in nested:

            outer_bound = get_range_bound(outer)
            inner_bound = get_range_bound(inner)

            if (outer_bound and inner_bound and outer_bound != inner_bound):
                return {"complexity": "O(n * m)"}

        for loop in loops:
            if (isinstance(loop, ast.While) and get_loop_step(loop) == "logarithmic"):

                return {"complexity": "O(n log n)"}
        return {"complexity": "O(n^2)"}

    for loop in loops:
        if isinstance(loop, ast.While):

            step = get_loop_step(loop)
            if step == "logarithmic":
                return {"complexity": "O(log n)"}

            if step == "linear":
                return {"complexity": "O(n)"}

        if isinstance(loop, ast.For):

            bound = get_range_bound(loop)
            if bound is not None:
                return {"complexity": "O(n)"}

    return {"complexity": "Needs further analysis"}
