// https://leetcode.com/problems/number-of-islands/description/
//
// Given an m x n 2D binary grid which represents a map of '1's (land) and
// '0's (water), return the number of islands.
//
// An island is surrounded by water and is formed by connecting adjacent lands
// horizontally or vertically. You may assume all four edges of the grid are all
// surrounded by water.
//
// Example 1
//
// Input: grid = [
//  ["1","1","1","1","0"],
//  ["1","1","0","1","0"],
//  ["1","1","0","0","0"],
//  ["0","0","0","0","0"]
// ]
// Output: 1
//
// Example 2
//
// Input: grid = [
//  ["1","1","0","0","0"],
//  ["1","1","0","0","0"],
//  ["0","0","1","0","0"],
//  ["0","0","0","1","1"]
// ]
//
// Output: 3
//
//
//  Solution:
//
//  Set islandCount to 0
//
//  Book keep all islands in a hash map islands.
//  In islands
//          key is row:col
//          value is the IslandCount detected for the cell
//
//  Iterate cell by cell along each row until we reach the end of the matrix.
//
//  For each encountered cell do the following
//          if cell is land and cell is not found in Islands collection:
//
//                  Increase islandCount by one
//
//                  Assign islands[row:col] for the cell to islandCount
//
//                  Use DFS (Depth First Search) to find all connected cells
//                  that are land. For each found cell fill in island[row:col]
//                  to islandCount to 		indicate that all these cells
//                  belong to the same island.
//
//          else if cell is found in the island collection skip to the next cell
//
//  Answer is the islandCount to be returned by the function

#include <gtest/gtest.h>
#include <map>
#include <vector>

using namespace std;

namespace {

struct pair_hash {
  template <class T1, class T2>
  std::size_t operator()(const std::pair<T1, T2> &pair) const {
    auto hash1 = std::hash<T1>{}(pair.first);
    auto hash2 = std::hash<T2>{}(pair.second);
    return hash1 ^ hash2; // Combine the two hash values
  }
};

using IslandMap = std::unordered_map<std::pair<int, int>, int, pair_hash>;

constexpr auto land = '1';
constexpr auto water = '0';

class Solution {
public:
  void searchContiguousLand(
      const vector<vector<char>> &grid,
      IslandMap &islands,
      int islandCount,
      int row,
      int col) {

    if (row < 0 ||  col < 0 || row >= grid.size() || col >= grid[row].size()) {
      return;
    }

    if (grid[row][col] == water || islands.contains(pair(row,col))) {
      return;
    }

    islands.emplace(pair(row,col), islandCount);

    // Up
    searchContiguousLand(grid, islands, islandCount, row, col - 1);

    // left
    searchContiguousLand(grid, islands, islandCount, row + 1, col);

    // down
    searchContiguousLand(grid, islands, islandCount, row, col + 1);

    // back
    searchContiguousLand(grid, islands, islandCount, row - 1, col);
  }

  int numIslands(vector<vector<char>> &grid) {
    int islandCount{0};
    IslandMap islands;

    for (auto row = 0; row < grid.size(); ++row) {
      for (auto col = 0; col < grid[row].size(); ++col) {
        if (grid[row][col] == water || islands.contains(pair(row, col))) {
          continue;
        }

        islandCount++;
        islands.emplace(pair(row, col), islandCount);

        // DFS search, no need to search up and backwards since those cells has
        // already been visited

        // Up
        searchContiguousLand(grid, islands, islandCount, row, col - 1);

        // left
        searchContiguousLand(grid, islands, islandCount, row + 1, col);

        // down
        searchContiguousLand(grid, islands, islandCount, row, col + 1);

        // back
        searchContiguousLand(grid, islands, islandCount, row - 1, col);
      }
    }

    return islandCount;
  }
};
} // namespace

TEST(NumberOfIslandsTest, EmptyGrid) {
  Solution solution;
  vector<vector<char>> input = {};
  EXPECT_EQ(0, solution.numIslands(input));
}

TEST(NumberOfIslandsTest, TC1) {
  Solution solution;
  vector<vector<char>> input = {
    {'1','1','1','1','0'},
    {'1','1','0','1','0'},
    {'1','1','0','0','0'},
    {'0','0','0','0','0'}};
  EXPECT_EQ(1, solution.numIslands(input));
}

TEST(NumberOfIslandsTest, TC2) {
  Solution solution;
  vector<vector<char>> input = {
    {'1','1','0','0','0'},
    {'1','1','0','0','0'},
    {'0','0','1','0','0'},
    {'0','0','0','1','1'}
  };

  EXPECT_EQ(3, solution.numIslands(input));
}


TEST(NumberOfIslandsTest, TC3) {
  Solution solution;
  vector<vector<char>> input = {
      {'1','1','1'},
      {'0','1','0'},
      {'1','1','1'}
  };

  EXPECT_EQ(1, solution.numIslands(input));
}






