# https://leetcode.com/problems/majority-element/description
# Given an array nums of size n, return the majority element.
#
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element
# always exists in the array.
#
# Example 1
# Input nums = [3,2,3]
# Output: 3
#
# Example 2
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
#
# Solution 1
# Introduce a dictionary (hashmap)
# Count elements using the element as key in the dictionary
# Return max element from the dictionary

from typing import List
from collections import defaultdict


def majority_element_1(nums: List[int]) -> int:
    element_count = defaultdict(int)
    majority_limit = len(nums) / 2

    for num in nums:
        element_count[num] += 1

        current_count = element_count[num]
        if current_count > majority_limit:
            return num
    return 0


# Use voting
# Introduce two variables:
# element_candidate = 0
# vote_count = 0
# Iterate through all elements
#  if element_candidate is zero assign element as element_candidate
#  increment vote_count if element is equal to element_candidate
#  decrement vote_count if element is not equal to element_candidate
# return element_candidate (instructions says that I can assume always a majority element)
def majority_element_2(nums: List[int]) -> int:
    element_candidate = 0
    vote_count = 0
    for num in nums:
        if vote_count == 0:
            element_candidate = num
        if element_candidate == num:
            vote_count += 1
        else:
            vote_count -= 1
    return element_candidate


if __name__ == "__main__":
    nums = [2, 2, 1, 1, 1, 2, 2]
    print(majority_element_1(nums))
    print(majority_element_2(nums))

    nums = [6, 5, 5]
    print(majority_element_2(nums))
