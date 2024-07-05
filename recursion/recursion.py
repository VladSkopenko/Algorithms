from functools import lru_cache


@lru_cache(maxsize=None)  # O(n)
def fibonacci(n: int) -> int:  # O(2^n)
    """Дуже висока складність алгоритму(без декоратора)"""
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_memo(n: int, memo: dict = None) -> int:  # O(n)
    """Кешування робить цей алгоритм лінійної складностні"""
    if memo is None:
        memo = {}
    elif n in memo:
        return memo[n]
    elif n <= 1:
        return n
    value = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    memo[n] = value
    return value


if __name__ == "__main__":
    result = fibonacci(499)
    result2 = fibonacci_memo(499)
    print(result2)
    print(result)
