def find_first_recurring(array):
    found_items = {}

    for item in array:
        if item in found_items:
            return item
        else:
            found_items[item] = True


if __name__ == "__main__":
    example_1 = [2, 5, 1, 2, 3, 5, 1, 2, 4]
    print(find_first_recurring(example_1))

    example_2 = [2, 1, 1, 2, 3, 5, 1, 2, 4]
    print(find_first_recurring(example_2))
