# Given 2 arrays,
# create a function that let´s a user know (tru/false) whether these two arrays contains any common items.
# Example 1:
# array_1 = ['a', 'b', 'c', 'x']
# array_2 = ['z', 'y', 'i']
# should return false
#
# Example 2:
# array_1 = ['a', 'b', 'c, 'x']
# array_2 = ['z', 'y', 'x']
# should return true

# Solution/Reasoning
# Input two arrays of items
# Questions:
# - Sorted?
# - Chars? Or other types?
# - Multiple chars per item?
# Output true/false
#
# Naive solution
# - All combinations => O(n^2)
#
# - If arrays are sorted
# 1. Pick first element of the two arrays that is the largest as a base
# 2. For array not chosen as base compare the first element with base
# A) If any of the array iterators is at end of its array return false
# B) If the comparing element is equal to the base element return true
# C) If the comparing element is smaller than the base element increase iterator for the comparing array one step to
# next element and restart at 2
# D) If the comparing element is larger than the base element, pick the comparing element as base, increase iterator for
# the array that previously was base and restart at 2
# O(m+n)
#
# - If arrays are not sorted
# Introduce two sets, one for each array, s1 & s2
# Two arrays a1 and a2
# A) If first element of a1 is found in s2 return true
# B) if first element of a2 in found s2 return true
# C) insert first element of a1 in s1
# D) insert first element of a2 in s1
# E) move a1 and a2 to next element and repeat from A


# Solution assuming sorted arrays
def contains_common_items_for_sorted(array_1, array_2):
    i1 = 0
    i2 = 0

    while i1 < len(array_1) and i2 < len(array_2):
        if array_1[i1] == array_2[i2]:
            return True
        elif i1 == len(array_1)-1:
            i2 += 1
        elif i2 == len(array_2)-1:
            i1 += 1
        elif array_1[i1] > array_2[i2]:
            i2 += 1
        elif array_1[i1] < array_2[i2]:
            i1 += 1

    return False


# Solution without requiring sorted arrays
def contains_common_items(array_1, array_2):
    s1 = set()
    s2 = set()

    i1 = 0
    i2 = 0

    while i1 < len(array_1) and i2 < len(array_2):
        if array_1[i1] == array_2[i2]:
            return True
        elif array_1[i1] in s2:
            return True
        elif array_2[i2] in s1:
            return True
        s1.add(array_1[i1])
        s2.add(array_2[i2])

        if i1 == len(array_1)-1 or array_1[i1] > array_2[i2]:
            i2 += 1
        elif i2 == len(array_2)-1 or array_1[i1] < array_2[i2]:
            i1 += 1

    return False


if __name__ == "__main__":

    # Sorted arrays

    array_10 = ['a', 'b', 'c', 'x']
    array_20 = ['i', 'y', 'z']
    print(contains_common_items_for_sorted(array_10, array_20))

    array_11 = ['a', 'b', 'c', 'x']
    array_21 = ['z', 'y', 'x']

    print(contains_common_items_for_sorted(array_11, array_21))

    # Not sorted arrays

    array_12 = ['a', 'b', 'c', 'x']
    array_22 = ['z', 'y', 'i']
    print(contains_common_items(array_12, array_22))

    array_13 = ['a', 'b', 'c', 'x']
    array_23 = ['z', 'y', 'x']

    print(contains_common_items(array_13, array_23))

    print("Case that is broken without sorting")
    array_14 = ['a', 'b', 'x', 'c']
    array_24 = ['z', 'y', 'x']
    print(contains_common_items(array_14, array_24))
    print(contains_common_items_for_sorted(sorted(array_14), sorted(array_24)))