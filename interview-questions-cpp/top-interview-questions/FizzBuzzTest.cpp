#include <gtest/gtest.h>
#include <string>
#include <vector>

using namespace std;

namespace {
vector<string> fizzBuzz(int n) {
  vector<string> result;
  for (auto i = 1; i <= n; ++i) {
    if (i % 15 == 0) {
      result.emplace_back("FizzBuzz");
    } else if (i % 3 == 0) {
      result.emplace_back("Fizz");
    } else if (i % 5 == 0) {
      result.emplace_back("Buzz");
    } else {
      result.emplace_back(to_string(i));
    }
  }
  return result;
}
} // namespace

TEST(FizzBuzz, Test3) {
  auto actual = fizzBuzz(3);
  vector<string> expected = {"1", "2", "Fizz"};
  ASSERT_EQ(expected, actual);
}

TEST(FizzBuzz, Test5) {
  auto actual = fizzBuzz(5);
  vector<string> expected = {"1", "2", "Fizz", "4", "Buzz"};
  ASSERT_EQ(expected, actual);
}

TEST(FizzBuzz, Test15) {
  auto actual = fizzBuzz(15);
  vector<string> expected = {"1",    "2",    "Fizz", "4",    "Buzz",
                             "Fizz", "7",    "8",    "Fizz", "Buzz",
                             "11",   "Fizz", "13",   "14",   "FizzBuzz"};
  ASSERT_EQ(expected, actual);
}