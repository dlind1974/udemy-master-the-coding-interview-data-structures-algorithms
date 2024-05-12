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
  vector<int> maxSlidingWindowPrioQueue(vector<int> &nums, int k) {
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

  vector<int> maxSlidingWindow(vector<int> &nums, int k) {
    vector<int> result;

    // Sliding window with indices of nums within the sliding window.
    deque<int> slidingWindow;

    for (auto i = 0; i < nums.size(); ++i) {
      // 1. Remove element at the top if it is outside of the window
      if (!slidingWindow.empty() && slidingWindow.front() <= i - k) {
        slidingWindow.pop_front();
      }

      // 2. Maintain the deque so that all items in the queue that is smaller than the current item is removed, they cannot contribute
      while (!slidingWindow.empty() && nums[slidingWindow.back()] < nums[i]) {
        slidingWindow.pop_back();
      }

      // 3. Add the current item to the back of the queue since all smaller items has been removed in step 2
      slidingWindow.push_back(i);

      // 4. If current item is not within the first k-1 entries add the top element if the deque to the result array
      if (i >= k - 1) {
        auto maxElement = slidingWindow.front();
        result.push_back(nums[maxElement]);
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
  const std::vector<int> expected  = {3,3,5,5,6,7};

  auto actual = solution.maxSlidingWindowPrioQueue(input, k);
  EXPECT_EQ(expected, actual);

  actual = solution.maxSlidingWindow(input, k);
  EXPECT_EQ(expected, actual);

}

TEST(MaxSlidingWindowTest, TC2) {
  std::vector<int> input = {1,-1};
  constexpr auto k = 1;
  Solution solution;
  const std::vector<int> expected  = {1, -1};

  auto actual = solution.maxSlidingWindowPrioQueue(input, k);
  EXPECT_EQ(expected, actual);

  actual = solution.maxSlidingWindow(input, k);
  EXPECT_EQ(expected, actual);
}

TEST(MaxSlidingWindowTest, TC3) {
  std::vector<int> input = {7,2,4};
  constexpr auto k = 2;
  Solution solution;
  const std::vector<int> expected  = {7, 4};

  auto actual = solution.maxSlidingWindowPrioQueue(input, k);
  EXPECT_EQ(expected, actual);

  actual = solution.maxSlidingWindow(input, k);
  EXPECT_EQ(expected, actual);
}