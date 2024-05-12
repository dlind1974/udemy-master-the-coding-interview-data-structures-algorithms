#include <gtest/gtest.h>

namespace handwritten {

int binarySearchImpl(const std::vector<int> &collection, int element,
                     size_t begin, size_t end) {

  if (begin >= end) {
    return -1;
  }

  auto size = end - begin;
  size_t middle = begin + size / 2;

  if (element == collection[middle]) {
    return middle;
  } else if (element > collection[middle]) {
    return binarySearchImpl(collection, element, middle + 1, end);
  } else {
    return binarySearchImpl(collection, element, begin, middle);
  }
}

/**
 * Searches for element in vector of integers.
 * @note This is handwritten to learn, real world uses algo in stdlib
 * @pre The input collection is sorted
 * @return The index of the element if element found else -1
 */
int binarySearch(const std::vector<int> &collection, int element) {
  if (collection.empty())
    return -1;
  return binarySearchImpl(collection, element, 0, collection.size());
}

} // namespace handwritten

// You have a vector with the ages of all people in the world.
// One entry per person. Write a function that counts the number of persons
// with a specified age.
// Assume that vector is sorted
//
// Solution:
// Do a binary search to find the age
// Do binary search to find the upper and lower bound for the age (first version
// using linear search)
namespace {

// Binary search to find one element, linear search to find upper and lower
// bound of the age. The age count is the distance between upper and lower
// bound.
// @note See ageCount3 using stl for preferred solution. This is just to learn.
int ageCount1(const std::vector<int> &ages, int ageToCount) {
  if (ages.empty()) {
    return 0;
  }

  // Find an entry of the age to be counted
  const auto ageIndex = handwritten::binarySearch(ages, ageToCount);

  // Search linearly downwards to get start index of age
  auto beginOfAge = ageIndex;
  while (beginOfAge > 0 && ages[beginOfAge - 1] == ageToCount) {
    beginOfAge--;
  }

  // Search linearly upwards to get end index of age
  auto endOfAge = ageIndex;
  const auto agesSize = ages.size();
  while (endOfAge < agesSize && ages[endOfAge] == ageToCount) {
    endOfAge++;
  }

  return endOfAge - beginOfAge;
}

int findLowBound(const std::vector<int> &collection, int elementToCount,
                 size_t begin, size_t end) {
  auto size = end - begin;
  size_t middle = begin + size / 2;

  if (middle == 0) {
    return 0;
  }

  if (elementToCount == collection[middle] &&
      elementToCount != collection[middle - 1]) {
    return middle;
  } else if (elementToCount > collection[middle]) {
    return findLowBound(collection, elementToCount, middle + 1, end);
  } else {
    return findLowBound(collection, elementToCount, begin, middle);
  }
}

int findHighBound(const std::vector<int> &collection, int elementToCount,
                  size_t begin, size_t end) {
  auto size = end - begin;
  size_t middle = begin + size / 2;

  if (middle == size - 1) {
    return size;
  }

  if (elementToCount == collection[middle] &&
      elementToCount != collection[middle + 1]) {
    // plus one since index represents the end which is one index past the last
    // element
    return middle + 1;
  } else if (elementToCount > collection[middle]) {
    return findHighBound(collection, elementToCount, middle + 1, end);
  } else {
    return findHighBound(collection, elementToCount, begin, middle);
  }
}

// Binary search to find one element, binary search to find upper and lower
// bound of the age. The age count is the distance between upper and lower
// bound.
// @note See ageCount3 using stl for preferred solution. This is just to learn.
int ageCount2(const std::vector<int> &ages, int ageToCount) {
  if (ages.empty()) {
    return 0;
  }

  auto ageIndex = handwritten::binarySearch(ages, ageToCount);
  if (ageIndex < 0) {
    return 0;
  }

  auto lowerBound = findLowBound(ages, ageToCount, 0, ageIndex);
  auto highBound = findHighBound(ages, ageToCount, ageIndex, ages.size());
  return highBound - lowerBound;
}

// Preferred solution using stl
int ageCount3(const std::vector<int> &ages, int ageToCount) {
  auto lowerBound = std::lower_bound(ages.cbegin(), ages.cend(), ageToCount);
  auto upperBound = std::upper_bound(ages.cbegin(), ages.cend(), ageToCount);
  return upperBound - lowerBound;
}
} // namespace

TEST(BinarySearchImplTests, CorrectIndexes) {

  {
    // Element is present in the collection
    std::vector<int> testInput = {1, 3, 5, 7, 9};
    const size_t searchElement = 7;
    const size_t expectedOutput = 3; // Index of 7 in the sorted array
    EXPECT_EQ(expectedOutput,
              handwritten::binarySearchImpl(testInput, searchElement, 0,
                                            testInput.size()));
    EXPECT_EQ(expectedOutput,
              handwritten::binarySearch(testInput, searchElement));
  }

  {
    // Element is not present, and the collection is large
    std::vector<int> testInput = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20};
    const size_t searchElement = 5;
    const size_t expectedOutput = -1; // 5 is not in the array
    EXPECT_EQ(expectedOutput,
              handwritten::binarySearchImpl(testInput, searchElement, 0,
                                            testInput.size()));
    EXPECT_EQ(expectedOutput,
              handwritten::binarySearch(testInput, searchElement));
  }

  {
    // Element is at the beginning of the collection
    std::vector<int> testInput = {0, 2, 4, 6, 8};
    const size_t searchElement = 0;
    const size_t expectedOutput = 0; // Index of 0
    EXPECT_EQ(expectedOutput,
              handwritten::binarySearchImpl(testInput, searchElement, 0,
                                            testInput.size()));
    EXPECT_EQ(expectedOutput,
              handwritten::binarySearch(testInput, searchElement));
  }

  {
    // Element is at the end of the collection
    std::vector<int> testInput = {1, 2, 3, 4, 5};
    const size_t searchElement = 5;
    const size_t expectedOutput = 4; // Index of 5
    EXPECT_EQ(expectedOutput,
              handwritten::binarySearchImpl(testInput, searchElement, 0,
                                            testInput.size()));
    EXPECT_EQ(expectedOutput,
              handwritten::binarySearch(testInput, searchElement));
  }

  {
    // Single element matching the search
    std::vector<int> testInput = {42};
    const size_t searchElement = 42;
    const size_t expectedOutput = 0; // Only one element which is a match
    EXPECT_EQ(expectedOutput,
              handwritten::binarySearchImpl(testInput, searchElement, 0,
                                            testInput.size()));
    EXPECT_EQ(expectedOutput,
              handwritten::binarySearch(testInput, searchElement));
  }

  {
    // Single element not matching the search
    std::vector<int> testInput = {100};
    const size_t searchElement = 101;
    const size_t expectedOutput = -1; // No match in a single-element vector
    EXPECT_EQ(expectedOutput,
              handwritten::binarySearchImpl(testInput, searchElement, 0,
                                            testInput.size()));
    EXPECT_EQ(expectedOutput,
              handwritten::binarySearch(testInput, searchElement));
  }

  {
    // Single element not matching the search
    std::vector<int> testInput = {100};
    const size_t searchElement = 101;
    const size_t expectedOutput = -1; // No match in a single-element vector
    EXPECT_EQ(expectedOutput,
              handwritten::binarySearchImpl(testInput, searchElement, 0,
                                            testInput.size()));
    EXPECT_EQ(expectedOutput,
              handwritten::binarySearch(testInput, searchElement));
  }

  {
    // Empty collection
    std::vector<int> testInput = {30};
    const size_t searchElement = 25;
    const size_t expectedOutput = -1; // No match in a single-element vector
    EXPECT_EQ(expectedOutput,
              handwritten::binarySearchImpl(testInput, searchElement, 0,
                                            testInput.size()));
    EXPECT_EQ(expectedOutput,
              handwritten::binarySearch(testInput, searchElement));
  }
}

TEST(AgeCountBasicTests, BasicScenarios) {
  // Test empty vector
  std::vector<int> agesEmpty = {};
  EXPECT_EQ(0, ageCount1(agesEmpty, 25));
  EXPECT_EQ(0, ageCount2(agesEmpty, 25));
  EXPECT_EQ(0, ageCount3(agesEmpty, 25));

  // Test single element vector with the matching age
  std::vector<int> agesSingleMatch = {25};
  EXPECT_EQ(1, ageCount1(agesSingleMatch, 25));
  EXPECT_EQ(1, ageCount2(agesSingleMatch, 25));
  EXPECT_EQ(1, ageCount3(agesSingleMatch, 25));

  // Test single element vector with no matching age
  std::vector<int> agesSingleNoMatch = {30};
  EXPECT_EQ(0, ageCount1(agesSingleNoMatch, 25));
  EXPECT_EQ(0, ageCount2(agesSingleNoMatch, 25));
  EXPECT_EQ(0, ageCount3(agesSingleNoMatch, 25));

  // Test multiple occurrences of the age
  std::vector<int> agesMultiple = {25, 25, 25, 26, 27, 28};
  EXPECT_EQ(3, ageCount1(agesMultiple, 25));
  EXPECT_EQ(3, ageCount2(agesMultiple, 25));
  EXPECT_EQ(3, ageCount3(agesMultiple, 25));

  // Test no occurrences of the age
  std::vector<int> agesNoOccurrences = {20, 21, 22, 23, 24};
  EXPECT_EQ(0, ageCount1(agesNoOccurrences, 25));
  EXPECT_EQ(0, ageCount2(agesNoOccurrences, 25));
  EXPECT_EQ(0, ageCount3(agesNoOccurrences, 25));

  // Test multiple ages, multiple counts
  std::vector<int> agesMixed = {20, 21, 21, 22, 23, 23, 23};
  EXPECT_EQ(3, ageCount1(agesMixed, 23));
  EXPECT_EQ(3, ageCount2(agesMixed, 23));
  EXPECT_EQ(3, ageCount3(agesMixed, 23));
}

// Define a single test case for large vector scenarios
TEST(AgeCountLargeVectorTests, LargeScenarios) {
  // Large vector with repetitive elements, sorted by nature of repetition
  std::vector<int> largeRepetitive(1000000, 30); // 1 million people aged 30
  EXPECT_EQ(1000000, ageCount3(largeRepetitive, 30));

  // Large vector with no occurrences of the search age, also sorted
  std::vector<int> largeNoMatch(1000000, 30); // 1 million people aged 30
  EXPECT_EQ(0, ageCount3(largeNoMatch, 31));

  // Large vector with a mixed distribution, needs sorting
  std::vector<int> largeMixed(1000000);
  std::fill(largeMixed.begin(), largeMixed.begin() + 500000,
            25); // 500,000 people aged 25
  std::fill(largeMixed.begin() + 500000, largeMixed.end(),
            26); // 500,000 people aged 26
  std::sort(largeMixed.begin(), largeMixed.end());
  EXPECT_EQ(500000, ageCount3(largeMixed, 25));
  EXPECT_EQ(500000, ageCount3(largeMixed, 26));

  // Large vector with sparse occurrences of the search age, needs sorting
  std::vector<int> largeSparse(1000000, 30); // Mostly people aged 30
  // Assign specific entries to a different age
  largeSparse[123456] = 25;
  largeSparse[234567] = 25;
  largeSparse[345678] = 25;
  // Ensure the vector is sorted after modifications
  std::sort(largeSparse.begin(), largeSparse.end());
  EXPECT_EQ(3, ageCount3(largeSparse, 25));
}
