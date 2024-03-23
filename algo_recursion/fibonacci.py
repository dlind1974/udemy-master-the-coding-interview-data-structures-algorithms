def fibonacci_iterative(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1

    fib_prev_prev = 0
    fib_prev = 1
    fib = 0
    for i in range(1, n):
        fib = fib_prev + fib_prev_prev
        fib_prev_prev = fib_prev
        fib_prev = fib

    return fib


def fibonacci_recursive(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


if __name__ == "__main__":
    print("Iterative")
    print(fibonacci_iterative(0))
    print(fibonacci_iterative(1))
    print(fibonacci_iterative(2))
    print(fibonacci_iterative(3))
    print(fibonacci_iterative(4))
    print(fibonacci_iterative(5))
    print(fibonacci_iterative(6))

    print("Rescursive")
    print(fibonacci_recursive(0))
    print(fibonacci_recursive(1))
    print(fibonacci_recursive(2))
    print(fibonacci_recursive(3))
    print(fibonacci_recursive(4))
    print(fibonacci_recursive(5))
    print(fibonacci_recursive(6))