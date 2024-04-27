// https://leetcode.com/problems/reverse-linked-list/description
// Reverse Linked List
//
// Example 1
// Input: head = [1,2,3,4,5]
// Output: [5,4,3,2,1]
//
// Example 2
// Input: head = [1,2]
// Output: [2,1]

#include <gtest/gtest.h>
#include <vector>
#include <algorithm>
#include <memory>

using namespace std;

namespace {

struct ListNode {
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};

ListNode* reverseList(ListNode *head) {
  ListNode* reversedHead = nullptr;
  ListNode* previous = nullptr;

  while (head) {
    reversedHead = head;
    auto nextHead = head->next;
    reversedHead->next = previous;
    previous = head;
    head = nextHead;
  }

  return reversedHead;
}

void freeNode(ListNode* head) {
  while(head) {
    ListNode* toDelete = head;
    head = head->next;
    delete toDelete;
  }
  return;
}

ListNode* createLinkedList(const std::vector<int>& values) {
  ListNode* head{nullptr};
  ListNode* back{nullptr};
  for (const auto value : values) {
    if (!head) {
      head = back = new ListNode(value);
    } else {
      back->next = new ListNode(value);
      back = back->next;
    }
  }
  return head;
}

std::vector<int> toValues(ListNode* head) {
  std::vector<int> values;

  while (head) {
    values.emplace_back(head->val);
    head = head->next;
  }

  return values;
}

} // namespace

TEST(ReverseLinkedList, CreateLinkedList) {
  const std::vector<int> expectedValues = {1,2,3,4,5};
  auto list = std::shared_ptr<ListNode>(
      createLinkedList(expectedValues),
      [](ListNode* head) {freeNode(head);});
  const auto actualValues = toValues(list.get());
  ASSERT_EQ(expectedValues, actualValues);
}

TEST(ReverseLinkedList, TestCase1) {
  auto forwardList = createLinkedList({1,2,3,4,5});
  auto reversedList = std::shared_ptr<ListNode>(
      reverseList(forwardList),
      [](ListNode* head) {freeNode(head);});

  const auto actualValues = toValues(reversedList.get());
  const std::vector<int> expectedValues = {5,4,3,2,1};
  ASSERT_EQ(expectedValues, actualValues);
}