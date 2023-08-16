from __future__ import annotations
from typing import Optional, Literal
from collections import deque


class TreeNode:
    def __init__(self, value: int = 0) -> None:
        self.value = value
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None


def balance_height(root: TreeNode):
    pass


def is_balanced(root: TreeNode) -> bool:
    pass


def isSymmetric_helper(left: Optional[TreeNode], right: Optional[TreeNode]):
    pass


def isSymmetric(root: Optional[TreeNode]) -> bool:
    pass


def treeSum(root: TreeNode):
    pass


def display(
    root: TreeNode,
    traversal_type: Literal["in-order", "post-order", "dfs", "bfs"] = "in-order",
):
    if root:
        if traversal_type == "in-order":
            display(root.left, traversal_type)
            print(root.value)
            display(root.right, traversal_type)
        elif traversal_type == "post-order":
            display(root.left, traversal_type)
            display(root.right, traversal_type)
            print(root.value)
        elif traversal_type == "dfs":
            stack = [root]
            while stack:
                curr = stack.pop()
                print(curr.value)
                if curr.left:
                    stack.append(curr.left)
                if curr.right:
                    stack.append(curr.right)
        elif traversal_type == "bfs":
            queue = deque([root])
            while queue:
                curr = queue.popleft()
                print(curr.value)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

        else:
            raise ValueError(f"Traversal Type:{traversal_type} not implemented")


if __name__ == "__main__":
    root = TreeNode(5)
    node1 = TreeNode(2)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(4)
    node6 = TreeNode(3)

    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    node2.left = node5
    node2.right = node6

    display(root, traversal_type="bfs")
