from __future__ import annotations
from typing import List, Optional


class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next: Optional[Node] = None


class LinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None

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
    print(ll)
