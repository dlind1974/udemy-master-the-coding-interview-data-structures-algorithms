// https://leetcode.com/problems/merge-intervals/
//
// Given an array of intervals where intervals[i] = [starti, endi], merge all
// overlapping intervals, and return an array of the non-overlapping.
//
// intervals that cover all the intervals in the input.
//
// Example 1:
// Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
// Output: [[1,6],[8,10],[15,18]]
// Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
//
// Example 2:
// Input: intervals = [[1,4],[4,5]]
// Output: [[1,5]]
// Explanation: Intervals [1,4] and [4,5] are considered overlapping.

// Solution:
// Assume intervals are sorted, otherwise I first have to sort them by start
// value. If sorted is required this will give complexity O(n log n)
//
// Put resolved intervals in a result array
//
// For each interval in intervals
//    Check if first element is in the range of the last interval in result
//    array If in last interval extend the last interval to the end of the
//    current interval If not in the last interval add the interval to result
//    array
//
// Time Complexity
// Sorting O(n log n)
// Iterating O(n)
// => Total time complexity O(n log n)
//
// Space Complexity
// Storing result O(n)

#include <gtest/gtest.h>

using namespace std;

namespace {

// Solution using initial sorting of intervals
vector<vector<int>> merge(vector<vector<int>> &intervals) {
  vector<vector<int>> result;
  std::sort(intervals.begin(), intervals.end(),
            [](const auto& a, const auto& b) { return a[0] < b[0];});

  for (const auto& interval : intervals) {
    if (result.empty()) {
      result.emplace_back(std::move(interval));
      continue;
    }

    if (interval[0] >= result.back()[0] && interval[0] <= result.back()[1]) {
      result.back()[1] = max(interval[1], result.back()[1]);
    } else {
      result.emplace_back(std::move(interval));
    }
  }
  return result;
}

} // namespace

TEST(MergeIntervals, Example1) {
  // Input: [[1,3],[2,6],[8,10],[15,18]]
  vector<vector<int>> input = {{1, 3}, {2, 6}, {8, 10}, {15, 18}};
  auto actualIntervals = merge(input);
  // Expected  result: [[1,6],[8,10],[15,18]]
  const vector<vector<int>> expectedIntervals = {{1,6},{8,10},{15,18}};
  EXPECT_EQ(expectedIntervals, actualIntervals);
}

TEST(MergeIntervals, TC1) {
  // Input: [[1,4],[0,4]]
  vector<vector<int>> input = {{1, 4}, {0, 4}};
  auto actualIntervals = merge(input);
  // Expected  result: [[0,4]]
  const vector<vector<int>> expectedIntervals = {{0,4}};
  EXPECT_EQ(expectedIntervals, actualIntervals);
}

TEST(MergeIntervals, TC2) {
  // [[1,4],[2,3]]
  vector<vector<int>> input = {{1, 4}, {2, 3}};
  auto actualIntervals = merge(input);
  // Expected  result: [[1,4]]
  const vector<vector<int>> expectedIntervals = {{1,4}};
  EXPECT_EQ(expectedIntervals, actualIntervals);
}
