from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def from_array(array: List[int]) -> TreeNode:
    for i in range(len(array)):
        pass
