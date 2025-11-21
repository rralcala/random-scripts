from typing import Optional

# Definition for a binary tree node.
from tree_toolkit import TreeNode


class Solution:
    def mergeTrees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        if root1 is None:
            root1 = TreeNode(0, None, None)
        if root2 is None:
            root2 = TreeNode(0, None, None)
        self.inOrder(root1, root2)
        return None

    def inOrder(self, root1, root2):
        root1.val += root2.val
        if root1.left is not None and root2.left is not None:
            if root1.left is None:
                root1.left = TreeNode(0)
            if root1.left is None:
                root1.left = TreeNode(0)
