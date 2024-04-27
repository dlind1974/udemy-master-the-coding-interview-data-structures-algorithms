# https://leetcode.com/problems/excel-sheet-column-number/
# Given a string column_title that represents the column title as appears in an Excel sheet, return its corresponding
# column number.
#
# Example:
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28
#
# Clarification to self. Excel sheets have columns A-Z. When Z is reached and you add next column, the new column is AA.
# Example: [A ... Z AA AB AC ...]
#
# Solution Explanation:
# Each letter from A to Z is assigned a numerical value: A = 1, B = 2, ..., Z = 26.
# Excel columns are labeled like a base-26 numeral system, where the rightmost letter has the lowest significance.
#
# Formula to convert column title to number:
# Contribution of each letter to the column number is calculated as:
#     letter_value * (base ^ position_from_end)
# where `letter_value` is the numeric equivalent (A=1, ..., Z=26),
# `base` is 26 because there are 26 letters,
# `position_from_end` is zero-indexed from the right (rightmost character is at position 0).
#
# Illustrations:
# Single letter columns:
# A -> 1  ; 1 * 26^0 = 1
# B -> 2  ; 2 * 26^0 = 2
# ...
# Z -> 26 ; 26 * 26^0 = 26
#
# Two-letter columns:
# AA -> 27 ; (1 * 26^1) + (1 * 26^0) = 27
# AB -> 28 ; (1 * 26^1) + (2 * 26^0) = 28
# ...
# ZY -> 701; (26 * 26^1) + (25 * 26^0) = 701
#
# The total number for a column is the sum of contributions from all its letters.


def title_to_number(column_title: str) -> int:
    number = 0
    base = ord('Z') - ord('A') + 1
    length = len(column_title)

    for i in range(length):
        # Calculate the value of each letter, adjusted for position
        value = ord(column_title[i]) - ord('A') + 1
        # Multiply by base raised to the power of the position from the end
        number += value * (base ** (length - i - 1))

    return number


def print_number_by_title(column_title: str) -> None:
    print(f"Title: {column_title}; number:{title_to_number(column_title)}")


if __name__ == "__main__":
    print("###########################")
    print(f"ord('A'):{ord('A')}")
    print(f"ord('B'):{ord('B')}")
    print(f"ord('Z'):{ord('Z')}")
    print(f"ord('Z')- ord('A'):{ord('Z') - ord('A')}")
    print("###########################")

    print_number_by_title("A")
    print_number_by_title("B")
    print_number_by_title("Z")
    print_number_by_title("AA")
    print_number_by_title("AB")
    print_number_by_title("ZY")