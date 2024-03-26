def fibonacci_iterative(n):
    calculations = 0

    if n <= 0:
        return 0
    if n == 1:
        return 1

    fib_prev_prev = 0
    fib_prev = 1
    fib = 0
    for i in range(1, n):
        calculations += 1
        fib = fib_prev + fib_prev_prev
        fib_prev_prev = fib_prev
        fib_prev = fib

    print(f"Calculations: {calculations}")

    return fib


def fibonacci_recursive(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


def fibonacci_recursive_calculator():
    calculations = 0
    cache = {}

    def fibonacci_recursive(n):
        nonlocal calculations

        if n in cache:
            return cache[n]

        calculations += 1
        print(f"calculation count: {calculations}")

        if n <= 0:
            cache[0] = 0
            return cache[0]
        if n == 1:
            cache[1] = 1
            return cache[1]
        cache[n] = fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
        return cache[n]

    return fibonacci_recursive


if __name__ == "__main__":
    print("Iterative")
    print(fibonacci_iterative(0))
    print(fibonacci_iterative(1))
    print(fibonacci_iterative(2))
    print(fibonacci_iterative(3))
    print(fibonacci_iterative(4))
    print(fibonacci_iterative(5))
    print(fibonacci_iterative(6))

    print("Recursive")
    print(fibonacci_recursive(0))
    print(fibonacci_recursive(1))
    print(fibonacci_recursive(2))
    print(fibonacci_recursive(3))
    print(fibonacci_recursive(4))
    print(fibonacci_recursive(5))
    print(fibonacci_recursive(6))

    print("Recursive with checks")
    calculator = fibonacci_recursive_calculator()
    print("fibonacci 5")
    print(calculator(5))
    print("fibonacci 55")
    print(calculator(55))
    print("fibonacci 15")
    print(calculator(15))
