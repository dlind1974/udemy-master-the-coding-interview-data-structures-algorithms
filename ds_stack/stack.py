class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        return self.top if self.top is None else self.top.value

    def push(self, value):
        node = Node(value)
        if self.top is not None:
            node.next = self.top
        self.top = node

        if self.bottom is None:
            self.bottom = node

        self.length += 1

    def pop(self):
        result = None
        if self.top is not None:
            result = self.top.value
            self.top = self.top.next
            self.length -= 1
        if self.top is None:
            self.bottom = None
        return result

    def is_empty(self):
        return self.length == 0


if __name__ == "__main__":
    stack = Stack()
    print(f"is_empty: {stack.is_empty()}")

    stack.push(1)
    print(f"peek: {stack.peek()}")
    print(f"is_empty: {stack.is_empty()}")

    stack.push(2)
    print(f"peek: {stack.peek()}")
    print(f"is_empty: {stack.is_empty()}")

    stack.push(3)
    print(f"peek: {stack.peek()}")
    print(f"is_empty: {stack.is_empty()}")

    print(f"pop: {stack.pop()}")
    print(f"peek: {stack.peek()}")
    print(f"pop: {stack.pop()}")
    print(f"peek: {stack.peek()}")
    print(f"pop: {stack.pop()}")
    print(f"peek: {stack.peek()}")
    print(f"pop: {stack.pop()}")

    print(f"is_empty: {stack.is_empty()}")
