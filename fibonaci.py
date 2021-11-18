import time
from functools import lru_cache

# get fibonaci number without memoization
def fibonaci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonaci(n - 1) + fibonaci(n - 2)


# get number with auto memoization
@lru_cache(maxsize=None)  # Decorator to apply automatic memoization
def fibonaci_memo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonaci_memo(n - 1) + fibonaci_memo(n - 2)


# Generate sequence of fibonacci numbers without memoization
def get_sequence(l):
    sequence = []
    for i in range(l):
        sequence.append(fibonaci(i))
    return sequence


# Generate sequence with automatic memoization
def get_sequence_memo(l):
    sequence = []
    for i in range(l):
        sequence.append(fibonaci_memo(i))
    return sequence


if __name__ == "__main__":
    start_a = time.time()
    fibonaci_list_a = get_sequence(40)
    end_a = time.time()
    start_b = time.time()
    fibonaci_list_b = get_sequence_memo(40)
    end_b = time.time()

    print(f"Execution time without memoization: {end_a - start_a}")
    print(f"Execution time with auto memoization: {end_b - start_b}")
