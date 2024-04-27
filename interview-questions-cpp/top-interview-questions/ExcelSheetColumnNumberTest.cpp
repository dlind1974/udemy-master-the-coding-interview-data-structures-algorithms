// https://leetcode.com/problems/excel-sheet-column-number/description/

#include <gtest/gtest.h>
#include <cmath>

using namespace std;

namespace {

int ord(char c) {
  return static_cast<int>(c);
}

const auto ColumnBase = ord('Z') - ord('A') + 1;

int titleToNumber(string columnTitle) {
  int result{0};
  int position = columnTitle.size() - 1;
  const auto AAsciiNumber = ord('A');
  auto toNumber = [AAsciiNumber](char letter) -> int { return ord(letter) - AAsciiNumber + 1;};

  for (auto letter : columnTitle) {
    result += toNumber(letter) * pow(ColumnBase, position);
    position--;
  }
  return result;
}


} // namespace

TEST(ExcelSheelColumnNumber, HandleNumbers) {
  char a = 'A';
  char z = 'Z';
  std::cout << ord(a) << std::endl;
  std::cout << ord(z) << std::endl;
  std::cout << ord(a) - ord(a) << std::endl;
  std::cout << ord('B') - ord(a) << std::endl;
  std::cout << ord(z) - ord(a) << std::endl;
}

TEST(ExcelSheelColumnNumber, TestCases) {
  ASSERT_EQ(1, titleToNumber("A"));
  ASSERT_EQ(2, titleToNumber("B"));
  ASSERT_EQ(3, titleToNumber("C"));
  ASSERT_EQ(26, titleToNumber("Z"));
  ASSERT_EQ(27, titleToNumber("AA"));
  ASSERT_EQ(28, titleToNumber("AB"));
  ASSERT_EQ(701, titleToNumber("ZY"));
}