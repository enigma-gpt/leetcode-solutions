# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        avg = []
        stack = [root]

        while len(stack) > 0:

            summ = 0
            i = 0
            temp = []
            while len(stack) > 0:
                node = stack.pop()
                summ += node.val
                i += 1
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)

            avg.append(summ/i)
            stack = temp

        return avg











