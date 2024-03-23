# Write two functions that finds the factorial of any number. One should use recursive, the other should just use a
# for loop

def find_factorial_recursive(number):
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    if number <= 1:
        return 1
    return number*find_factorial_recursive(number-1)


def find_factorial_iterative(number):
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    result = 1
    for number in range(1, number+1):
        result *= number
    return result


if __name__ == "__main__":
    print("Recursive")
    print(find_factorial_recursive(0))
    print(find_factorial_recursive(1))
    print(find_factorial_recursive(2))
    print(find_factorial_recursive(3))
    print(find_factorial_recursive(4))
    print(find_factorial_recursive(5))

    print("Iterative")
    print(find_factorial_iterative(0))
    print(find_factorial_iterative(1))
    print(find_factorial_iterative(2))
    print(find_factorial_iterative(3))
    print(find_factorial_iterative(4))
    print(find_factorial_iterative(5))
