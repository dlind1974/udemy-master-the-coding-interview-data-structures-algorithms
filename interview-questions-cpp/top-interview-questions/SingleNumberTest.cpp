//  https://leetcode.com/problems/single-number
#include <gtest/gtest.h>
#include <vector>
#include <set>

using namespace std;

namespace {
int singleNumber(vector<int>& nums) {
  set<int> duplicates;
  for (auto num : nums) {
    if (duplicates.contains(num)) {
      duplicates.erase(num);
    }
    else {
      duplicates.insert(num);
    }
  }
  return *duplicates.begin();
}

//The XOR operation has a few critical properties that are useful here:
//A number XORed with itself results in 0 (e.g., x ^ x = 0).
//A number XORed with 0 remains unchanged (e.g., x ^ 0 = x).
//XOR is commutative and associative, which means the order in which you XOR the numbers does not change the result.
int singleNumberSpeedup(vector<int>& nums) {
  int result = 0;

  for (auto num : nums) {
    result ^= num;
  }

  return result;
}

} // namespace

TEST(SingleNumber, TC1) {
  vector<int> numbers = {2,2,1};
  auto actual = singleNumber(numbers);
  auto expected = 1;
  ASSERT_EQ(expected, actual);

  auto actualSpeedup = singleNumberSpeedup(numbers);
  ASSERT_EQ(expected,actualSpeedup);
}

TEST(SingleNumber, TC2) {
  vector<int> numbers = {4,1,2,1,2};
  auto actual = singleNumber(numbers);
  auto expected = 4;
  ASSERT_EQ(expected, actual);

  auto actualSpeedup = singleNumberSpeedup(numbers);
  ASSERT_EQ(expected,actualSpeedup);
}


