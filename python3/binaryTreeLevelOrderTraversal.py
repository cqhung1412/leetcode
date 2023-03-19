from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getValues(self, valueList: List[List[int]], index: int, root: Optional[TreeNode]):
        if root is not None:
            if len(valueList) != index + 1:
                valueList.append([])
            valueList[index].append(root.val)
            self.getValues(valueList, index+1, root.left)
            self.getValues(valueList, index+1, root.right)

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        valueList: List[List[int]] = []
        index = 0
        self.getValues(valueList, index, root)
        return [ele for ele in valueList if ele != []]
