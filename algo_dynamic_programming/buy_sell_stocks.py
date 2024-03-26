# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description
#
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future
# to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Example 1:
#
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:
#
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
#
# Idea:
# Loop through the price array once
# For each stock price in the price array log min_value and max_profit

from typing import List


def max_profit(prices: List[int]) -> int:
    if len(prices) == 0:
        return 0

    max_profit_result = 0
    min_value = prices[0]

    for value in prices:
        if value < min_value:
            min_value = value

        max_profit_result = max(max_profit_result, value-min_value)

    return max_profit_result


if __name__ == "__main__":
    stock_prices = [7, 1, 5, 3, 6, 4]
    print(max_profit(stock_prices))

    stock_prices = [7, 6, 4, 3, 1]
    print(max_profit(stock_prices))
