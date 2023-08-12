from __future__ import annotations
from typing import List, Optional


class CircularQueue:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1
        self.size = 0

    def enqueue(self, value):
        if self.size == self.capacity:
            print("Queue is full.")
            return

        if self.rear == -1:
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = value
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            print("Queue is empty.")
            return

        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity

        self.size -= 1

    def peek(self):
        if self.size == 0:
            print("Queue is empty.")
        return self.queue[self.front]

    def display(self):
        if self.size == 0:
            print("Queue is empty.")
            return

        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.capacity
        print()


if __name__ == "__main__":
    c = CircularQueue(capacity=5)
    c.enqueue(1)
    c.enqueue(2)
    c.enqueue(3)
    c.display()
    c.dequeue()
    c.display()
    c.enqueue(4)
    c.enqueue(5)
    c.display()
    c.enqueue(6)
    c.display()
    c.dequeue()
    c.display()
    c.enqueue(7)
    c.display()
