# https://leetcode.com/problems/fizz-buzz/description/
#
# Given an integer n, return a string array answer (1-indexed) where:
#
# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.
#
# Example 1:
#
# Input: n = 3
# Output: ["1","2","Fizz"]
# Example 2:
#
# Input: n = 5
# Output: ["1","2","Fizz","4","Buzz"]
# Example 3:
#
# Input: n = 15
# Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

from typing import List


def fizz_buzz(n: int) -> List[str]:
    result = []
    for i in range(1, n+1):
        divisible_by_three = i % 3 == 0
        divisible_by_five = i % 5 == 0
        if  divisible_by_three and divisible_by_five:
            result.append("FizzBuzz")
        elif divisible_by_three:
            result.append("Fizz")
        elif divisible_by_five:
            result.append("Buzz")
        else:
            result.append((str(i)))

    return result


def fizz_buzz_clean(n: int) -> List[str]:
    return [
        "FizzBuzz" if i % 3 == 0 and i % 5 == 0 else
        "Fizz" if i % 3 == 0 else
        "Buzz" if i % 5 else
        str(i)
        for i in range(1, n + 1)
    ]


def fizz_buzz_clean_speed(n: int) -> List[str]:
    return [
        "FizzBuzz" if i % 15 == 0 else
        "Fizz" if i % 3 == 0 else
        "Buzz" if i % 5 else
        str(i)
        for i in range(1, n + 1)
    ]


if __name__ == '__main__':
    print(fizz_buzz_clean_speed(3))
    print(fizz_buzz_clean_speed(5))
    print(fizz_buzz_clean_speed(15))

