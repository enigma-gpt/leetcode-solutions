# Definition for a binary tree node.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if p is None and q is None:
            return True

        if (p is None and q is not None) or (p is not None and q is None):
            return False

        stackP = [p]
        stackQ = [q]

        while len(stackP) > 0 or len(stackQ) > 0:

            if len(stackP) != len(stackQ):
                return False

            tempP, tempQ = [], []

            while len(stackP) > 0 or len(stackQ) > 0:

                pElement = stackP.pop()
                qElement = stackQ.pop()

                if pElement.val != qElement.val:
                    return False

                if pElement.left is not None:
                    pElement.left.val = str(pElement.left.val) + "L"
                    tempP.append(pElement.left)

                if pElement.right is not None:
                    pElement.right.val = str(pElement.right.val) + "R"
                    tempP.append(pElement.right)

                if qElement.left is not None:
                    qElement.left.val = str(qElement.left.val) + "L"
                    tempQ.append(qElement.left)

                if qElement.right is not None:
                    qElement.right.val = str(qElement.right.val) + "R"
                    tempQ.append(qElement.right)

            stackP = tempP
            stackQ = tempQ

        return True
