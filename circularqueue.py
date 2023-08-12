class CircularQueue:
    def __init__(self, size: int) -> None:
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def enqueue(self):
        pass

    def dequeue(self):
        pass

    def peek(self):
        pass

    def __str__(self):
        if self.front == -1:
            return "Queue is empty!"


if __name__ == "__main__":
    c = CircularQueue(size=5)
    print(c)
