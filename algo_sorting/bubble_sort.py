def bubble_sort(array):
    unsorted_length = len(array)
    while unsorted_length > 0:
        for j in range(0, unsorted_length):
            if j+1 >= unsorted_length:
                continue
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
        unsorted_length -= 1
    return array


if __name__=="__main__":
    my_array = [3, 5, 2, 4, 6, 8, 4]
    print(bubble_sort(my_array))