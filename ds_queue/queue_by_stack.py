# https://leetcode.com/problems/implement-queue-using-stacks/description/

# Idea:
# Use two stacks, front_stack and back_stack
# When pushing new items to queue move all items from front_stack to back_stack.
# When front_stack is empty push the new item. Then pop and push all items from the back_stack one by one to the
# front stack.

class MyQueue:

    def __init__(self):
        # Treat Python list as stack
        self.front_stack = []
        self.back_stack = []

    def push(self, x: int) -> None:
        while len(self.front_stack) > 0:
            self.back_stack.append(self.front_stack.pop())
        self.front_stack.append(x)
        while len(self.back_stack) > 0:
            self.front_stack.append(self.back_stack.pop())

    def pop(self) -> int:
        return self.front_stack.pop()

    def peek(self) -> int:
        return self.front_stack[-1]

    def empty(self) -> bool:
        return len(self.front_stack) == 0


if __name__ == "__main__":
    queue = MyQueue()
    print(queue.empty())
    queue.push(10)
    print(queue.empty())
    queue.push(12)
    queue.push(14)
    print(queue.peek())
    print(queue.pop())
    print(queue.peek())
    print(queue.pop())
    print(queue.peek())
    print(queue.empty())
    print(queue.pop())
    print(queue.empty())

    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    print(queue.peek())
    print(queue.pop())
    print(queue.empty())

# Your MyQueue object will be instantiated and called as such:
