# https://leetcode.com/problems/climbing-stairs/description/
#
# You are climbing a staircase. It takes n steps to reach the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Example 1:
#
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:
#
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

# Idea:
# Iterate through each step 0 to n-1
# At each step store the number of possible solutions
# At each step check how many sub solutions there are backwards
# => Sub solution 1: For 1 step, set it to the number of solutions one step back
# => Sub solution 2: For 2 step, set it to the number of solutions two steps back
# The total number of solutions at each step is the sum of both sub solutions

def climb_stairs(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1

    solution_count_two_steps_back = 0
    solution_count_one_step_back = 1
    current_max = 1

    for step in range(2, n+1):
        sub_solution_1_step = solution_count_one_step_back
        sub_solution_2_step = solution_count_two_steps_back if step > 2 else 1
        current_max = sub_solution_1_step + sub_solution_2_step
        solution_count_two_steps_back = solution_count_one_step_back
        solution_count_one_step_back = current_max

    return current_max


if __name__ == "__main__":
    #print(climb_stairs(2))
    print(climb_stairs(3))
