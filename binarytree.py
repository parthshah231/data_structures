from __future__ import annotations
from typing import List, Optional

from collections import deque


class TreeNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.left = None
        self.right = None


def insert(root, val):
    if root is None:
        return TreeNode(val=val)
    if root.val > val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root


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


def sumTreeNodes(root):
    if root is None:
        return 0
    return root.val + root.left.val + root.right.val


def isSymmetricHelper(left, right):
    if left is None and right is None:
        return True

    if left is None or right is None:
        return False

    if left.val != right.val:
        return False

    return isSymmetricHelper(left.left, right.right) and isSymmetricHelper(
        left.right, right.left
    )


def isSymmetric(root):
    if not root:
        return True

    return isSymmetricHelper(root.left, root.right)


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
    root.left = TreeNode(2)
    root.right = TreeNode(2)

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
    # x = mergeTrees(node1, node4)
    # display(x)
    # print(sumTreeNodes(node4))
    print(isSymmetric(root))
