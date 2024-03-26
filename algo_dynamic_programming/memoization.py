def memoize_add_to_80():
    cache = {}

    def add_to_80(n):
        if n in cache:
            return cache[n]
        else:
            print('long time')
            answer = n + 80
            cache[n] = answer
            return answer

    return add_to_80


def fibonacci_calculator():
    calculations = 0

    def fibonacci(n):
        nonlocal calculations
        calculations += 1
        print(f"calculation count: {calculations}")
        if n < 2:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)

    return fibonacci


if __name__ == "__main__":
    # Usage
    add_to_80 = memoize_add_to_80()
    print(add_to_80(10))
    print(add_to_80(10))  # This call will fetch the result from cache

    fib_calc = fibonacci_calculator()
    print(fib_calc(4))