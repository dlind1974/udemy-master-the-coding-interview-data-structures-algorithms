def reverse_string(str):
    result = []
    for i in reversed(range(len(str))):
        result.append(str[i])
    return "".join(result)


def reverse_string_recursive(str):
    if len(str) < 1:
        return str
    return str[-1] + reverse_string_recursive(str[:-1])


if __name__ == "__main__":
    print("Iterative")
    print(reverse_string("hello"))
    print(reverse_string("this is my string!"))

    print("Recursive")
    print(reverse_string_recursive("hello"))
    print(reverse_string_recursive("this is my string!"))
