def merge(left, right):
    result = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result += left[left_index:]
    result += right[right_index:]
    return result


def merge_sort_by_index(array, start, end):
    if end - start == 1:
        return array[start:end]

    split_index = start + int((end - start) / 2)

    return merge(
        merge_sort_by_index(array, start, split_index),
        merge_sort_by_index(array, split_index, end)
    )


def merge_sort(array):
    return merge_sort_by_index(array, 0, len(array))


if __name__ == "__main__":
    print("merge")
    print(merge([3, 5], [4, 5, 7, 9]))
    print(merge([3, 5, 6, 8], [4, 5]))
    print(merge([], []))
    print(merge([1], []))
    print(merge([], [2]))

    print("sort")
    print(merge_sort([3, 5, 2, 4]))
    print(merge_sort([3, 5, 2, 4, 2, 10, 1]))
