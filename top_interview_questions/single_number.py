# https://leetcode.com/problems/single-number/description/
#
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
#
# You must implement a solution with a linear runtime complexity and use only constant extra space.
#
# Example 1:
#
# Input: nums = [2,2,1]
# Output: 1
# Example 2:
#
# Input: nums = [4,1,2,1,2]
# Output: 4
# Example 3:
#
# Input: nums = [1]
# Output: 1

# Solution:
# Use a set to indicate duplicates
# set first element as candidate solution
# Loop through all elements
# If element not found in set add set
# If element found in set remove element
# When all elements looped through the set contains one element that is the solution

from typing import List


def single_number(nums: List[int]) -> int:
    duplicates = set()
    for num in nums:
        if num in duplicates:
            duplicates.remove(num)
        else:
            duplicates.add(num)
    return duplicates.pop()


if __name__ == "__main__":
    nums = [2, 2, 1]
    print(single_number(nums))

    nums = [4, 1, 2, 1, 2]
    print(single_number(nums))

    nums = [1]
    print(single_number(nums))