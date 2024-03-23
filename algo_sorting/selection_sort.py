def selection_sort(array):
    array_length = len(array)
    for i in range(array_length):
        min = array[i]
        min_position = i
        for j in range(i, array_length):
            if array[j] < min:
                min = array[j]
                min_position = j
        array[i], array[min_position] = array[min_position], array[i]
    return array


if __name__=="__main__":
    my_array = [3, 5, 2, 4, 6, 8, 4]
    print(selection_sort(my_array))
