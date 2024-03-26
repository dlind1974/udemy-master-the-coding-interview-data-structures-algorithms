# https://leetcode.com/problems/house-robber/
from typing import List


# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
# the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and
# it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can
# rob tonight without alerting the police.

# Example 1:
#
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# Example 2:
#
# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.

# Idea:
# Introduce a cache to store max value of robbed houses at each house index.
# Loop through the houses from start to end.
# At each index in the house list store the max of the two alternatives house[i] + house[i-1] and house[i] + house[i-2].

def rob(nums: List[int]) -> int:
    total_max = 0
    cache = {}

    for i in range(len(nums)):
        two_houses_back = cache.get(i - 2, 0)
        three_houses_back = cache.get(i - 3, 0)
        current_max = max(nums[i] + two_houses_back, nums[i] + three_houses_back)
        cache[i] = current_max
        if current_max > total_max:
            total_max = current_max

    return total_max


if __name__ == "__main__":
    houses = [1, 2, 3, 1]
    print(rob(houses))

    houses = [2, 7, 9, 3, 1]
    print(rob(houses))
