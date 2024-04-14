#include <gtest/gtest.h>
#include <vector>

using namespace std;

namespace {
void reverseString(vector<char>& s) {
  std::size_t n = s.size();
  auto mid = n / 2;
  for (auto i=0; i < mid; ++i) {
    std::swap(s[i], s[n-i-1]);
  }
}
}

TEST(ReverseString, HelloTest)
{
  vector<char> actual = {'h', 'e', 'l', 'l', 'o'};
  reverseString(actual);
  vector<char> expected = {'o', 'l', 'l', 'e', 'h'};
  ASSERT_EQ(expected, actual);
}