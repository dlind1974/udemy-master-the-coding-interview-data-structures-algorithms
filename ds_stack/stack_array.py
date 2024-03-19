class Stack:
    def __init__(self):
        self.data = []

    def peek(self):
        if len(self.data) > 0:
            return self.data[-1]
        return None

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if len(self.data) > 0:
            return self.data.pop(-1)

    def is_empty(self):
        return len(self.data) != 0


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
