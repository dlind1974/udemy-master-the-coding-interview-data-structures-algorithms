def insert_last_as_sorted(array):
    # should have used splice method
    # TODO: Check splice for python list

    # Could do binary search instead, but keep linear search for simplicity
    if len(array) <= 1:
        return array

    element_to_insert = array[-1]
    for i in reversed(range(len(array) - 1)):
        if element_to_insert < array[i]:
            array[i + 1], array[i] = array[i], array[i + 1]

    return array


def insert_last_as_sorted_by_ref(array, end_index):
    # Could do binary search instead, but keep linear search for simplicity
    if end_index <= 1:
        return array

    element_to_insert = array[end_index - 1]
    for i in reversed(range(end_index - 1)):
        if element_to_insert < array[i]:
            array[i + 1], array[i] = array[i], array[i + 1]
        else:
            break

    return array


def insertion_sort(array):
    for i in range(len(array)):
        insert_last_as_sorted_by_ref(array, i + 1)
    return array


if __name__ == "__main__":
    print("Testing insert_last_as_sorted_by_ref")
    print(insert_last_as_sorted_by_ref([], 1))
    print(insert_last_as_sorted_by_ref([2], 1))
    print(insert_last_as_sorted_by_ref([3, 2], 2))
    print(insert_last_as_sorted_by_ref([2, 3], 2))
    print(insert_last_as_sorted_by_ref([2, 5, 8, 4], 4))

    print("Run insertion sort")
    print(insertion_sort([]))
    print(insertion_sort([5]))
    print(insertion_sort([5, 2]))
    print(insertion_sort([3, 5, 2, 4, 6, 8, 4]))
