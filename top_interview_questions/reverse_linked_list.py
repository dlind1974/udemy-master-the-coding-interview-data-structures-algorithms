# https://leetcode.com/problems/reverse-linked-list/description/
#
# Reverse Linked List
#
# Example 1
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
#
# Example 2
# Input: head = [1,2]
# Output: [2,1]

from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list_recursive(head: Optional[ListNode]) -> (ListNode, ListNode):
    if head.next is None:
        return head, head

    first, last = reverse_list_recursive(head.next)
    last.next = head
    head.next = None
    return first, last.next


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    return reverse_list_recursive(head)[0]


def reverse_list_recursive_2(head: Optional[ListNode], prev: Optional[ListNode] = None) -> Optional[ListNode]:
    if not head:
        return prev
    next_node = head.next
    head.next = prev
    return reverse_list_recursive_2(next_node, head)


def reverse_list_2(head: Optional[ListNode]) -> Optional[ListNode]:
    return reverse_list_recursive_2(head)


# Submitted solution
def reverse_list_3(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    new_head = None

    while head is not None:
        new_head = head
        head = head.next
        new_head.next = prev
        prev = new_head

    return new_head


def create_linked_list(values: List) -> Optional[ListNode]:
    if values is None:
        return None

    head = current = ListNode(values[0], None)

    for value in values[1:]:
        current.next = ListNode(value, None)
        current = current.next

    return head


def print_linked_list(head: ListNode):
    print("################")
    while head is not None:
        print(head.val)
        head = head.next
    print("################")


if __name__ == "__main__":
    example_1 = create_linked_list([1, 2, 3, 4, 5])
    print_linked_list(example_1)

    reversed_1 = reverse_list_3(example_1)
    print_linked_list(reversed_1)
