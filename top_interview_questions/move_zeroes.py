# https://leetcode.com/problems/move-zeroes/description/
#
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero
# elements.
#
# Note that you must do this in-place without making a copy of the array.
#
# Example 1:
#
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:
#
# Input: nums = [0]
# Output: [0]
#
# Solution:
# Iterate through all numbers
# Use two indexes:
# - index => The current position in the loop
# - zeroes_start_index => The first position of zeroes
# When first zero is found set zeroes_start_index
# When nums[index] is non zero and there is a zeroes_start_index, swap values for the two indices and increment
# zeroes_start_index

from typing import List


def move_zeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    zeroes_start = None

    for index in range(0, len(nums)):
        if zeroes_start is None and nums[index] == 0:
            zeroes_start = index

        if zeroes_start is not None and nums[index] != 0:
            nums[index], nums[zeroes_start] = nums[zeroes_start], nums[index]
            zeroes_start += 1


def move_zeroes_simplified(nums: List[int]) -> None:
    insert_pos = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            if i != insert_pos:
                nums[insert_pos], nums[i] = nums[i], nums[insert_pos]
            insert_pos += 1


if __name__ == "__main__":
    test_data = [0, 1, 0, 3, 12]
    move_zeroes(test_data)
    print(test_data)

    test_data = [0, 1, 0, 3, 12]
    move_zeroes_simplified(test_data)
    print(test_data)

    test_data = [0]
    move_zeroes(test_data)
    print(test_data)

    test_data = [0]
    move_zeroes_simplified(test_data)
    print(test_data)
