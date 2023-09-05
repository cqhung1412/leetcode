
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def check(self, leftNode: Optional[TreeNode], rightNode: Optional[TreeNode]) -> bool:
        if leftNode is None and rightNode is None:
            return True
        if leftNode is None or rightNode is None:
            return False
        if leftNode.val != rightNode.val:
            return False
        return self.check(leftNode.right, rightNode.left) and self.check(leftNode.left, rightNode.right)
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.check(root.left, root.right)