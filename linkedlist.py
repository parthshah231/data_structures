from __future__ import annotations
from typing import List, Optional


class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next: Optional[Node] = None


class LinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None

    def append(self, value: int) -> None:
        new: Node = Node(value=value)
        if self.head is None:
            self.head = new
            return

        node: Node = self.head
        while node.next is not None:
            node = node.next
        node.next = new

    def remove(self, idx: int) -> None:
        if self.head is None:
            raise IndexError(f"{idx} is out of bounds")

        if idx == 0:
            if self.head.next is None:
                self.head = None
            else:
                self.head = self.head.next
            return

        i = 0
        node: Node = self.head
        prev_node: Node = None

        while node.next is not None and i < idx:
            prev_node = node
            node = node.next
            i += 1

        if node is None:
            raise IndexError(f"{idx} is out of bounds")

        prev_node.next = node.next

    def __str__(self) -> str:
        if self.head is None:
            return "[[]]"

        node: Node = self.head
        fmt = ["[["]

        while node.next is not None:
            fmt.append(f"{node.value}, ")
            node = node.next

        fmt.append(f"{node.value}]]")
        return "".join(fmt)


if __name__ == "__main__":
    ll = LinkedList()
    ll.append(value=1)
    print(ll)
    ll.remove(idx=0)
    print(ll)
    ll.append(value=2)
    ll.append(value=3)
    ll.remove(idx=0)
    ll.append(value=4)
    ll.append(value=5)
    ll.remove(idx=1)
    ll.remove(idx=1)
    print(ll)
