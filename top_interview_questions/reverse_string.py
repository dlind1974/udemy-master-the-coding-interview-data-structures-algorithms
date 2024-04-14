# https://leetcode.com/problems/reverse-string/description/
#
# Write a function that reverses a string. The input string is given as an array of characters s.
#
# You must do this by modifying the input array in-place with O(1) extra memory.
#
# Example 1:
#
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:
#
# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]

from typing import List


def reverse_string(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    length = len(s)
    for i in range(length):
        swap_index = length - i - 1
        if i <= swap_index:
            s[i], s[swap_index] = s[swap_index], s[i]
        else:
            break


def reverse_string_improved(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    mid = len(s) // 2
    for i in range(mid):
        s[i], s[-i-1] = s[-i-1], s[i]


if __name__ == '__main__':
    s = ["h", "e", "l", "l", "o"]
    reverse_string(s)
    print(s)

    s = ["H", "a", "n", "n", "a", "h"]
    reverse_string_improved(s)
    print(s)

    s = ["h", "e", "l", "l"]
    reverse_string_improved(s)
    print(s)



