class CircularQueue:
    def __init__(self, size: int) -> None:
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def enqueue(self, value):
        if self.rear == self.size - 1:
            print(f"Queue is full. Cannot add {value} to the queue.")
            return

        if self.front == -1:
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value

    def dequeue(self):
        if self.front == -1:
            print("Queue is empty.")
            return
        elif self.front == self.rear:
            # temp = self.queue[self.front]
            self.front = self.rear = -1
        else:
            # temp = self.queue[self.front]
            self.front = (self.front + 1) % self.size

        # return temp

    def peek(self):
        if self.front == -1:
            print("Queue is empty.")
            return
        return self.queue[self.front]

    def __str__(self):
        if self.front == -1:
            return "Queue is empty!"

        i = self.front
        queue = []
        while True:
            queue.append(f"{self.queue[i]} ")
            if i == self.rear:
                break
            i = (i + 1) % self.size

        return ", ".join(queue)


if __name__ == "__main__":
    c = CircularQueue(size=5)
    c.enqueue(5)
    c.enqueue(10)
    c.dequeue()
    c.enqueue(15)
    print(c.peek())
    print(c)
