from __future__ import annotations
from typing import List, Optional

from collections import deque


class TreeNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.left = None
        self.right = None


def insert():
    pass


def findMinValue(root):
    if root is None:
        return

    leftMin = findMinValue(root.left) if root.left is not None else float("inf")
    rightMin = findMinValue(root.right) if root.right is not None else float("inf")
    return min(root.val, leftMin, rightMin)


def mergeTrees(root1, root2):
    if root1 is None and root2 is None:
        return

    if root1 is None:
        return root2

    if root2 is None:
        return root1

    s = TreeNode(root1.val + root2.val)
    s.left = mergeTrees(root1.left, root2.left)
    s.right = mergeTrees(root1.right, root2.right)

    return s


def display(root, traversal_type="bfs"):
    if root is None:
        print("Empty tree.")
        return

    if traversal_type == "bfs":
        queue = deque([root])
        while queue:
            curr = queue.popleft()
            print(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
    else:
        raise ValueError(f"{traversal_type} not implemented.")


if __name__ == "__main__":
    root = TreeNode(-1)

    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)

    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)

    node1.left = node2
    node1.right = node3

    node4.left = node5
    node4.right = node6

    # print(findMinValue(root))
    x = mergeTrees(node1, node4)
    display(x)
