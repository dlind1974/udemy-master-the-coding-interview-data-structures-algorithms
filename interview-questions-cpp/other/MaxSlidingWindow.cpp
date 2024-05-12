// https://leetcode.com/problems/sliding-window-maximum/description/
//
// You are given an array of integers nums,
// there is a sliding window of size k which is moving from the very left of
// the array to the very right.You can only see the k numbers in the
// window.Each time the sliding window moves right by one position.
//
// Return the max sliding window.
//
// Example 1:
//
//    Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
//    Output: [3,3,5,5,6,7]
//    Explanation:
//    Window position                Max
//    ---------------               -----
//    [1  3  -1] -3  5  3  6  7      3
//    1 [3  -1  -3] 5  3  6  7       3
//    1  3 [-1  -3  5] 3  6  7       5
//    1  3  -1 [-3  5  3] 6  7       5
//    1  3  -1  -3 [5  3  6] 7       6
//    1  3  -1  -3  5 [3  6  7]      7

// Idea:
// Use a deque to keep the k elements of the window
// Indices of elements are stored in the deque
// Largest element index should be at the top of the queue
// Ensure that the largest element's index is always at the front of the deque.
// Removing indices from the front if they are out of the bounds => keep on removing until in bounds
// Use a priority queue in order to have largest element on top

#include <gtest/gtest.h>
#include <vector>
#include <queue>

using namespace std;

namespace {

struct Node {
  int value;
  int index;
};

using NodeContainer = std::vector<Node>;

auto max_heap_compare = [](const Node &left, const Node &right) {
  return left.value < right.value;
};

class Solution {
public:
  vector<int> maxSlidingWindow(vector<int> &nums, int k) {
    vector<int> result;

    using container = std::vector<Node>;
    priority_queue<Node, container, decltype(max_heap_compare)> slidingWindow{
        max_heap_compare};

    for (auto i = 0; i < nums.size(); ++i) {
      slidingWindow.push(Node{nums[i], i});

      if (i >= k - 1) {
        while (slidingWindow.top().index <= i - k) {
          slidingWindow.pop();
        }

        result.emplace_back(slidingWindow.top().value);
      }
    }

    return result;
  }
};

} // namespace

TEST(MaxSlidingWindowTest, TC1) {
  std::vector<int> input = {1,3,-1,-3,5,3,6,7};
  constexpr auto k = 3;
  Solution solution;
  auto actual = solution.maxSlidingWindow(input, k);
  const std::vector<int> expected  = {3,3,5,5,6,7};
  EXPECT_EQ(expected, actual);
}

TEST(MaxSlidingWindowTest, TC2) {
  std::vector<int> input = {1,-1};
  constexpr auto k = 1;
  Solution solution;
  auto actual = solution.maxSlidingWindow(input, k);
  const std::vector<int> expected  = {1, -1};
  EXPECT_EQ(expected, actual);
}
