from typing import List
import unittest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        return self.tree(self.preorder(root, []))

    def preorder(self, root: TreeNode, result: List):
        if root.left is not None:
            self.preorder(root.left, result)
        result.append(root.val)
        if root.right is not None:
            self.preorder(root.right, result)
        return result

    def tree(self, arr):
        if not arr:
            return None

        mid = int((len(arr)) / 2)
        root = TreeNode(arr[mid])
        root.left = self.tree(arr[:mid])
        root.right = self.tree(arr[mid + 1 :])
        return root


class Tests(unittest.TestCase):
    def test1(self):
        root = TreeNode("1", None, None)
        l2 = TreeNode("2", None, None)
        l3 = TreeNode("3", None, None)
        l4 = TreeNode("5", None, None)
        l5 = TreeNode("4", None, None)
        root.right = l2
        l2.right = l3
        l3.right = l4
        l4.left = l5
        self.assertEqual("3", Solution().balanceBST(root).val)


if __name__ == "__main__":
    unittest.main()
