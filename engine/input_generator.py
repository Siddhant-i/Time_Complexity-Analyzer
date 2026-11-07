"""Generate test datasets of different sizes"""


import random

def generate_input(size, distribution = "random", seed = None):
    
    # dataset (size) = numberical foam - whole number (but Only positive numbers)
    if not isinstance(size, int) or isinstance(size, bool) or size < 0:
        raise ValueError("Size must be a non-negative integer")
    
    valid_distibution = {"random","sorted","reverse"}
    
    if distribution not in valid_distibution:
        raise ValueError("Distruibution must be 'random', 'sortrd', or 'reverse'")
    
    
    rng = random.Random(seed)
    numbers = [rng.randint(0,100000) for i in range(size)]
    
    if distribution == "sorted":
        numbers.sort()

    elif distribution == "reverse":
        numbers.sort(reverse=True)

    return numbers

