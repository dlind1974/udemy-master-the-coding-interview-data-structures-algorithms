// https://leetcode.com/problems/min-stack/description/
//
// Design a stack that supports push, pop, top, and retrieving the minimum
// element in constant time.
//
// Implement the MinStack class:
//
// MinStack() initializes the stack object.
// void push(int val) pushes the element val onto the stack.
// void pop() removes the element on the top of the stack.
// int top() gets the top element of the stack.
// int getMin() retrieves the minimum element in the stack.
// You must implement a solution with O(1) time complexity for each function.

// Notes
// Stack => FIFO, First In First Out
//
// Solution
// Use a list to represent the stack
// The elements in the stack are nodes where each node is aware of the min value
// for all elements that have been pushed to the stack so far.

#include <gtest/gtest.h>
#include <list>

namespace {

struct Node {
  int value;
  int minValue;
};

class MinStack {
public:
  MinStack() {}

  void push(int val) {
    auto newMin{val};
    if (!mStack.empty()) {
      newMin = val < mStack.front().minValue  ? val : mStack.front().minValue;
    }
    mStack.emplace_front(Node{val, newMin});
  }

  void pop() {
    mStack.pop_front();
  }

  int top() {
    return mStack.front().value;
  }

  int getMin() {
    return mStack.front().minValue;
  }

private:
  std::list<Node> mStack;
};

} // namespace

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */

TEST(MinStackTest, BasicFunctionality) {
  MinStack minStack;
  minStack.push(-2);
  minStack.push(0);
  minStack.push(-3);
  EXPECT_EQ(-3, minStack.getMin());
  minStack.pop();
  EXPECT_EQ(0, minStack.top());
  EXPECT_EQ(-2, minStack.getMin());
}
