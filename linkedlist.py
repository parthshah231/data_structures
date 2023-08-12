from __future__ import annotations
from typing import List, Optional


class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next: Optional[Node] = None


class LinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None

    def append(self, value: int):
        new: Node = Node(value=value)
        if self.head is None:
            self.head = new
            return

        node = self.head
        while node.next is not None:
            node = node.next
        node.next = new

    def remove(self, idx: int):
        if self.head is None:
            return

        if idx == 0:
            self.head = self.head.next
            return

        node: Node = self.head
        prev_node: Node = None
        i = 0

        while node.next is not None and i < idx:
            prev_node = node
            node = node.next
            i += 1

        if node is None:
            raise ValueError(f"Index {idx} is out of bounds of the linked list")

        prev_node.next = node.next

    def __str__(self) -> str:
        node = self.head
        if node is None:
            return "[[]]"

        fmt = ["[["]
        while node.next is not None:
            fmt.append(f"{node.value}, ")
            node = node.next

        fmt.append(f"{node.value}]]")
        return "".join(fmt)


if __name__ == "__main__":
    ll = LinkedList()
    ll.append(value=1)
    ll.append(value=2)
    ll.append(value=3)
    ll.remove(idx=1)
    ll.append(value=4)
    ll.remove(idx=1)
    ll.remove(idx=1)
    print(ll)
