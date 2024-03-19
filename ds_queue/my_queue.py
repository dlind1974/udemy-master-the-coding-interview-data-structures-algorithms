class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        return None if self.first is None else self.first.value

    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        dequeued_value = None
        if self.length > 0:
            dequeued_value = self.first.value

            if self.last == self.first:
                self.last = None

            self.first = self.first.next
            self.length -= 1

        return dequeued_value

    def is_empty(self):
        return self.length == 0


if __name__ == "__main__":
    queue = Queue()
    print(f"is_empty: {queue.is_empty()}")

    queue.enqueue(1)
    print(f"peek: {queue.peek()}")
    print(f"is_empty: {queue.is_empty()}")

    queue.enqueue(2)
    print(f"peek: {queue.peek()}")
    print(f"is_empty: {queue.is_empty()}")

    queue.enqueue(3)
    print(f"peek: {queue.peek()}")
    print(f"is_empty: {queue.is_empty()}")

    print(f"dequeue: {queue.dequeue()}")
    print(f"peek: {queue.peek()}")
    print(f"dequeue: {queue.dequeue()}")
    print(f"peek: {queue.peek()}")
    print(f"dequeue: {queue.dequeue()}")
    print(f"peek: {queue.peek()}")
    print(f"dequeue: {queue.dequeue()}")

    print(f"is_empty: {queue.is_empty()}")
