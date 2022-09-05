from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:

        if root is None:
            return []

        stack = [root]
        out = []

        while len(stack) > 0:

            temp = []
            sub_array = []

            while len(stack) > 0:
                elem = stack.pop(0)
                children = elem.children
                temp.extend(children)
                sub_array.append(elem.val)

            stack = temp
            out.append(sub_array)

        return out



