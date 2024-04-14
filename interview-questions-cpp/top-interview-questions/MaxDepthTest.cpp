// https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
#include <gtest/gtest.h>
#include <memory>
#include <algorithm>

namespace {
struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode() : val(0), left(nullptr), right(nullptr) {}
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
  TreeNode(int x, TreeNode *left, TreeNode *right)
      : val(x), left(left), right(right) {}

  ~TreeNode() {
    if (left != nullptr){
      delete left;
      left = nullptr;
    }

    if (right != nullptr) {
      delete right;
      right = nullptr;
    }
  }
};


int maxDepth(TreeNode* root) {
  if (root== nullptr) {
    return 0;
  }

  return (1 + std::max(maxDepth(root->left), maxDepth(root->right)));
}

std::unique_ptr<TreeNode> createTreeTC1() {
  auto root = std::make_unique<TreeNode>(3);
  root->left = new TreeNode(9);
  root->right = new TreeNode(20);
  root->right->left = new TreeNode(15);
  root->right->right = new TreeNode(7);
  return root;
}

} // namespace

TEST(MaxDepth, TC1) {
  auto tree = createTreeTC1();
  auto actualDepth = maxDepth(tree.get());
  ASSERT_EQ(3, actualDepth);
}