import heapq


def merge_sorted_arrays(array1, array2):
    result = []
    index1 = 0
    index2 = 0

    while index1 < len(array1) or index2 < len(array2):
        if index1 >= len(array1):
            result = result + array2[index2:]
            index2 = len(array2)
        elif index2 >= len(array2):
            result = result + array1[index1:]
            index1 = len(array1)
        elif array1[index1] < array2[index2]:
            result.append(array1[index1])
            index1 += 1
        else:
            result.append(array2[index2])
            index2 += 1

    return result


def merge_sorted_arrays_2(array1, array2):
    result = []
    index1 = 0
    index2 = 0

    while index1 < len(array1) or index2 < len(array2):
        if index2 >= len(array2) or array1[index1] < array2[index2]:
            result.append(array1[index1])
            index1 += 1
        elif index1 >= len(array1) or array2[index2] <= array1[index1]:
            result.append(array2[index2])
            index2 += 1

    return result


def merge_sorted_arrays_idiomatic(array1, array2):
    return list(heapq.merge(array1, array2))


if __name__ == "__main__":
    print(merge_sorted_arrays([0, 3, 4, 31], [4, 6, 30]))
    print(merge_sorted_arrays_2([0, 3, 4, 31], [4, 6, 30]))
    print(merge_sorted_arrays_idiomatic([0, 3, 4, 31], [4, 6, 30]))