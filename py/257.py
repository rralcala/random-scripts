from typing import List


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        result = []
        if root == None:
            return result
        self._binaryTreePaths(root, [], result)
        return result

    def _binaryTreePaths(self, root, path: List[str], result: List[str]) -> List[str]:
        path.append(str(root.val))
        printpath = True
        if root.left:
            self._binaryTreePaths(root.left, path, result)
            printpath = False
        if root.right:
            self._binaryTreePaths(root.right, path, result)
            printpath = False
        if printpath:
            result.append("->".join(path))
        path.pop()
