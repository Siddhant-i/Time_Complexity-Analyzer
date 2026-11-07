"""The validator checks whether an algorithm produces the correct output"""


def  validate_sorting(original, result):
    expected = sorted(original)
    return result == expected

def validate_searching(arr, target, result):

    if target not in arr:
        return result == -1
    
    return (
        isinstance(result, int) and not isinstance(result, bool) 
        and 0 <= result < len(arr)
        and arr[result] == target )
    
def validate_result(actual, expected):
    
    return actual == expected

